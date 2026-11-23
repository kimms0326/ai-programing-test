import csv

import pytest


def read_scores(path):
	kept = []
	skipped = []

	with open(path, "r", encoding="utf-8", newline="") as csv_file:
		reader = csv.reader(csv_file)
		next(reader, None)  # Consume the header.

		for row in reader:
			if not row:
				skipped.append(row)
				continue

			if len(row) != 2:
				skipped.append(row)
				continue

			name, score_text = row
			name = name.strip()
			score_text = score_text.strip()

			if not name or not score_text:
				skipped.append(row)
				continue

			try:
				score = int(score_text)
			except ValueError:
				skipped.append(row)
				continue

			if not 0 <= score <= 100:
				skipped.append(row)
				continue

			kept.append((name, score))

	return kept, skipped


def _csv_file(tmp_path, contents):
	path = tmp_path / "scores.csv"
	path.write_text(contents, encoding="utf-8")
	return path


def test_reads_valid_rows_and_quoted_comma_in_name(tmp_path):
	path = _csv_file(
		tmp_path,
		'name,score\nAlice,90\n"Smith, Jane",100\nZero,0\n',
	)

	kept, skipped = read_scores(path)

	assert kept == [("Alice", 90), ("Smith, Jane", 100), ("Zero", 0)]
	assert skipped == []


def test_records_blank_and_invalid_rows_without_stopping(tmp_path):
	path = _csv_file(
		tmp_path,
		"name,score\n"
		"\n"
		"MissingScore,\n"
		"NotANumber,abc\n"
		"TooLow,-1\n"
		"TooHigh,101\n"
		"Extra,fields,here\n"
		"Valid,75\n",
	)

	kept, skipped = read_scores(path)

	assert kept == [("Valid", 75)]
	# All six malformed lines, including the blank line, must be recorded.
	assert len(skipped) == 6
	assert skipped


def test_header_only_file_returns_empty_lists(tmp_path):
	path = _csv_file(tmp_path, "name,score\n")

	assert read_scores(path) == ([], [])


def test_missing_file_raises_file_not_found_error(tmp_path):
	with pytest.raises(FileNotFoundError):
		read_scores(tmp_path / "missing.csv")

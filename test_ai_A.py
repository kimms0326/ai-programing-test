import csv

import pytest


MIN_SCORE = 0
MAX_SCORE = 100


def load_scores(path):
    """성적 CSV를 읽어 (유효한 목록, 건너뛴 줄 기록) 을 돌려준다."""
    kept = []
    skipped = []

    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for line_no, row in enumerate(reader, start=1):
            if line_no == 1:
                continue
            if not row:
                continue

            original = ",".join(row)

            if len(row) != 2:
                skipped.append((line_no, original, "열 개수가 2가 아님"))
                continue

            name = row[0].strip()
            raw = row[1].strip()

            if name == "":
                skipped.append((line_no, original, "이름이 비어 있음"))
                continue
            if raw == "":
                skipped.append((line_no, original, "점수가 비어 있음"))
                continue

            try:
                score = int(raw)
            except ValueError:
                skipped.append((line_no, original, "점수가 정수가 아님"))
                continue

            if score < MIN_SCORE or score > MAX_SCORE:
                skipped.append((line_no, original, "점수가 0~100 밖"))
                continue

            kept.append((name, score))

    return kept, skipped


def write_csv(tmp_path, text):
    path = tmp_path / "scores.csv"
    path.write_text(text, encoding="utf-8-sig")
    return path


def test_load_scores_normal(tmp_path):
    path = write_csv(tmp_path, "name,score\nAlice,90\nBob,75\n")

    kept, skipped = load_scores(path)

    assert kept == [("Alice", 90), ("Bob", 75)]
    assert skipped == []


@pytest.mark.parametrize("score", [0, 100])
def test_load_scores_boundary_values(tmp_path, score):
    path = write_csv(tmp_path, f"name,score\nStudent,{score}\n")

    kept, skipped = load_scores(path)

    assert kept == [("Student", score)]
    assert skipped == []


def test_load_scores_skips_invalid_rows(tmp_path):
    path = write_csv(
        tmp_path,
        "name,score\n"
        "\n"
        "Alice,\n"
        ",50\n"
        "Bob,nope\n"
        "Carol,-1\n"
        "Dave,101\n"
        "Eve,80,extra\n"
        "Frank,60\n",
    )

    kept, skipped = load_scores(path)

    assert kept == [("Frank", 60)]
    assert skipped == [
        (3, "Alice,", "점수가 비어 있음"),
        (4, ",50", "이름이 비어 있음"),
        (5, "Bob,nope", "점수가 정수가 아님"),
        (6, "Carol,-1", "점수가 0~100 밖"),
        (7, "Dave,101", "점수가 0~100 밖"),
        (8, "Eve,80,extra", "열 개수가 2가 아님"),
    ]


def test_load_scores_file_not_found(tmp_path):
    missing = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_scores(missing)

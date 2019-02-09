# https://stackoverflow.com/questions/54607954/define-a-function-to-parse-an-email-adress/54608282#54608282

import pytest

def parse_email(s):
  parts = s.strip().split('@', 1)
  if len(parts) == 2:
    return (parts[0], parts[1])
  else:
    raise ValueError()

def test_parse_simple_email():
  parts = parse_email("cheese@peas.com")
  assert len(parts) == 2
  assert parts[0] == "cheese"
  assert parts[1] == "peas.com"

def test_invalid_email():
  with pytest.raises(ValueError):
    parts = parse_email("this is not an e-mail address")

def test_parse_email_with_whitespace():
  parts = parse_email(" cheese@peas.com ")
  assert len(parts) == 2
  assert parts[0] == "cheese"
  assert parts[1] == "peas.com"
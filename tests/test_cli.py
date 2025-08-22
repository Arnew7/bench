import pytest
from bench.cli import parse_args, load_hosts

def test_parse_args_hosts():
    args = parse_args(["-H", "https://ya.ru,https://example.com", "-C", "2"])
    assert args.count == 2
    assert "ya.ru" in args.hosts

def test_load_hosts_from_hosts():
    args = parse_args(["-H", "https://ya.ru"])
    hosts = load_hosts(args)
    assert hosts == ["https://ya.ru"]

def test_load_hosts_invalid():
    args = parse_args(["-H", "ftp://bad.url"])
    with pytest.raises(ValueError):
        load_hosts(args)

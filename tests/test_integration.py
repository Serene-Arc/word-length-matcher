#!/usr/bin/env python3
# coding=utf-8
import argparse

import pytest

import wordlengthmatcher.__main__ as main


@pytest.fixture()
def args() -> argparse.Namespace:
    args = argparse.Namespace()
    args.verbosity = 0
    args.file = './austen.txt'
    args.match_string = ''
    args.text = None
    return args


@pytest.mark.parametrize('test_match_string', (
    '4 5 2 3 3 3 2',
))
def test_simple_run_length(test_match_string: str, args: argparse.Namespace, capsys: pytest.CaptureFixture):
    args.match_string = test_match_string
    main.main(args)
    output = capsys.readouterr()
    assert 'This eBook is for the use of' in output.out


@pytest.mark.parametrize('test_text', (
    'vqp vparmpukgqbx unbi ugrgyk cugm vp knmlclsteh',
))
def test_simple_run_text(test_text: str, args: argparse.Namespace, capsys: pytest.CaptureFixture):
    args.text = test_text
    main.main(args)
    output = capsys.readouterr()
    assert '1 matches found' in output.out

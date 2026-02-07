import pytest
from app.main import main
from io import StringIO
import sys

def run_main_with_input(monkeypatch, capsys, input_text):
    simulated_input = input_text + "\nexit"
    monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
    main()
    return capsys.readouterr().out

def test_main_add(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "add 5 3")
    assert "Result: 8.0" in output

def test_main_subtract(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "sub 10 4")
    assert "Result: 6.0" in output

def test_main_multiply(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "mul 3 3")
    assert "Result: 9.0" in output

def test_main_divide(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "div 10 2")
    assert "Result: 5.0" in output

def test_main_divide_by_zero(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "div 5 0")
    assert "Cannot divide by zero" in output

def test_main_unknown_operation(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "magic 1 2")
    assert "Unknown operation" in output

def test_main_invalid_numbers(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "add ten five")
    assert "Error" in output

def test_main_invalid_format(monkeypatch, capsys):
    output = run_main_with_input(monkeypatch, capsys, "add 5")
    assert "Invalid format" in output

from app.calculator import Calculator

def test_main_unexpected_error(monkeypatch, capsys):
    def mock_add(a, b):
        raise Exception("Something went wrong!")
    
    monkeypatch.setattr(Calculator, 'add', mock_add)

    inputs = StringIO("add 1 1\nexit\n")
    monkeypatch.setattr('sys.stdin', inputs)
    
    main()
    
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Something went wrong!" in captured.out
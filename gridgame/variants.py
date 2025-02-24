from abc import ABC, abstractmethod

from .project_types import PlayerId, Cell, Symbol, Feedback, Field

class SymbolPlacer(ABC):
    @abstractmethod
    def place_symbol(self, symbol: Symbol, cell: Cell, is_game_over: bool, symbol_choices: list[Symbol], field: Field) -> Feedback:
        ...

class TicTacToeSymbolPlacer(SymbolPlacer):
    def place_symbol(self, symbol: Symbol, cell: Cell, is_game_over: bool, symbol_choices: list[Symbol], field: Field) -> Feedback:
        if is_game_over:
            return Feedback.GAME_OVER

        if symbol not in symbol_choices:
            return Feedback.INVALID_SYMBOL

        if not field.is_within_bounds(cell):
            return Feedback.OUT_OF_BOUNDS

        if field.get_symbol_at(cell) is not None:
            return Feedback.OCCUPIED

        field.place_symbol(symbol, cell)

        return Feedback.VALID

class WildSymbolPlacer(SymbolPlacer):
    def place_symbol(self, symbol: Symbol, cell: Cell, is_game_over: bool, symbol_choices: list[Symbol], field: Field) -> Feedback:
        if is_game_over:
            return Feedback.GAME_OVER

        if symbol not in symbol_choices:
            return Feedback.INVALID_SYMBOL

        if not field.is_within_bounds(cell):
            return Feedback.OUT_OF_BOUNDS

        if field.get_symbol_at(cell) is not None:
            return Feedback.OCCUPIED

        field.place_symbol(symbol, cell)

        return Feedback.VALID
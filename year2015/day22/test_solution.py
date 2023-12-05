import pytest
from .solution import (
    Game,
    Player,
    Spell,
    MagicMissile,
    Drain,
    Shield,
    Poison,
    Recharge,
    play_two_turns,
    get_winner,
)


@pytest.mark.parametrize(
    "game_state, spells, expected_game_states",
    [
        (
            {
                "Henry": Player(hit_points=10, armor=0, mana=250),
                "Boss": Player(hit_points=13, damage=8),
                "multiturn_spells": [],
                "spell_history": [],
            },
            [Poison(), MagicMissile()],
            [
                {
                    "Henry": Player(hit_points=2, armor=0, mana=77),
                    "Boss": Player(hit_points=10, damage=8),
                    "multiturn_spells": [Poison(turns=5)],
                    "spell_history": [Poison()],
                },
                {
                    "Henry": Player(hit_points=-6, armor=0, mana=24),
                    "Boss": Player(hit_points=0, damage=8),
                    "multiturn_spells": [Poison(turns=3)],
                    "spell_history": [Poison(), MagicMissile()],
                },
            ],
        ),
        (
            {
                "Henry": Player(hit_points=10, armor=0, mana=250),
                "Boss": Player(hit_points=14, damage=8),
                "multiturn_spells": [],
                "spell_history": [],
            },
            [Recharge(), Shield(), Drain(), Poison(), MagicMissile()],
            [
                {
                    "Henry": Player(hit_points=2, armor=0, mana=122),
                    "Boss": Player(hit_points=14, damage=8),
                    "multiturn_spells": [Recharge(turns=4)],
                    "spell_history": [
                        Recharge(),
                    ],
                },
                {
                    "Henry": Player(hit_points=1, armor=7, mana=211),
                    "Boss": Player(hit_points=14, damage=8),
                    "multiturn_spells": [Recharge(turns=2), Shield(turns=5)],
                    "spell_history": [
                        Recharge(),
                        Shield(),
                    ],
                },
                {
                    "Henry": Player(hit_points=2, armor=7, mana=340),
                    "Boss": Player(hit_points=12, damage=8),
                    "multiturn_spells": [Shield(turns=3)],
                    "spell_history": [
                        Recharge(),
                        Shield(),
                        Drain(),
                    ],
                },
                {
                    "Henry": Player(hit_points=1, armor=7, mana=167),
                    "Boss": Player(hit_points=9, damage=8),
                    "multiturn_spells": [Shield(turns=1), Poison(turns=5)],
                    "spell_history": [
                        Recharge(),
                        Shield(),
                        Drain(),
                        Poison(),
                    ],
                },
                {
                    "Henry": Player(hit_points=-7, armor=0, mana=114),
                    "Boss": Player(hit_points=-1, damage=8),
                    "multiturn_spells": [Poison(turns=3)],
                    "spell_history": [
                        Recharge(),
                        Shield(),
                        Drain(),
                        Poison(),
                        MagicMissile(),
                    ],
                },
            ],
        ),
    ],
)
def test_play_two_turns(
    game_state: Game, spells: list[Spell], expected_game_states: list[Game]
):
    for spell, expected_game_state in zip(spells, expected_game_states):
        game_state = play_two_turns(game_state, spell, handicap_henry=0)
        assert game_state == expected_game_state
    assert get_winner(game_state) == "Henry"

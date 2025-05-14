# Naame: "Belal Abdullah Ragab";
# Sec : 2;
# ID: 4462;


import re
from typing import Set, Dict, Tuple

class DFA:
    def __init__(self, start_state, accept_states: Set, transitions: Dict[Tuple, str]):
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def accepts(self, s: str) -> bool:
        state = self.start_state
        for char in s:
            if (state, char) in self.transitions:
                state = self.transitions[(state, char)]
            else:
                return False
        return state in self.accept_states

def regex_to_dfa(regex: str) -> DFA:
    class RegexDFA:
        def __init__(self, pattern):
            self.pattern = "^" + pattern + "$"  

        def accepts(self, s: str) -> bool:
            return re.fullmatch(self.pattern, s) is not None

    return RegexDFA(regex)

assert regex_to_dfa("(a|b)*abb").accepts("aabb") == True
assert regex_to_dfa("(a|b)*abb").accepts("ababa") == False
print("Tests passed.")

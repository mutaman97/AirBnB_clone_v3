#!/usr/bin/python3
'''
    This script tests the functionality of counting objects
'''
import sys
from models import storage
from models.state import State

if __name__ == "__main__":
    # Count all objects
    all_count = storage.count()

    # Count State objects
    state_count = storage.count(State)

    print("All objects: {}".format(all_count))
    print("State objects: {}".format(state_count))

    # Print information about the first State object
    states = storage.all(State)
    if len(states) > 0:
        first_state_id = list(states.keys())[0]
        first_state = states[first_state_id]
        print("First state: [{}] ({}) {}".format(
            first_state.__class__.__name__, first_state.id, first_state.to_dict()))

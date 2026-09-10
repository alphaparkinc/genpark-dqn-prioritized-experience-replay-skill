from client import SumTree

def main():
    print("=== Testing Prioritized Experience Replay (PER) Sum Tree ===")
    tree = SumTree(capacity=8)

    tree.add(10.0, "transition_s0_a0")
    tree.add(45.0, "transition_s1_a1")
    tree.add(5.0,  "transition_s2_a2")

    print("Total priority mass:", tree.total_priority())
    assert tree.total_priority() == 60.0

    d_idx, prio, item = tree.sample(25.0)
    print(f"Sampled item at cumulative mass 25.0: '{item}' with priority {prio}")
    assert item == "transition_s1_a1"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()

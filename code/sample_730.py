def run_length_encode(text: str) -> list:
    encoded = []
    count = 1
    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            encoded.append((text[i], count))
            count = 1
    return encoded


if __name__ == "__main__":
    print(run_length_encode("A"))
    print(run_length_encode("ABB"))
    print(run_length_encode("ABBAAACCCC"))

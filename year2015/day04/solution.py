"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle input is bgvyzdsv.

--- Part Two ---

Now find one that starts with six zeroes.

--- Notes ---

Find the salt that makes the hash have at least five leading zeros.

"""
import hashlib


def solve(secret_key: str, prefix: str) -> int:

    salt = 0
    result = "0"
    while not result.startswith(prefix):
        salt += 1
        hash_function = hashlib.md5()
        hash_function.update(bytes(secret_key, "utf-8"))
        hash_function.update(bytes(str(salt), "utf-8"))
        result = hash_function.hexdigest()

    return salt


if __name__ == "__main__":

    print(f"Part 1:\nThe salt is {solve('bgvyzdsv', '00000')}!\n")
    print(f"Part 2:\nThe salt is {solve('bgvyzdsv', '000000')}!\n")

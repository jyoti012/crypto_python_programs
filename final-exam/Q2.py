def cube_root_mod_p(y, p):
    """Finds the cube root of y mod p.

    Args:
        y: An integer.
        p: A prime number.

    Returns:
        The cube root of y mod p.
    """

    # Convert the hex numbers to decimal.
    y = int(y, 16)
    p = int(p, 16)

    # Find the cube root of y mod p.
    root = pow(y, (2 * p - 1) // 3, p)

    # Convert the cube root back to hex.
    root_hex = hex(root)[2:]

    # Return the first five hex characters of the cube root.
    return root_hex


if __name__ == '__main__':
    y = 'd'
    p = 'b2fd46ca29a3cb763d3de3d2c0883109573f55353f85237136e75e1ef3e5b2ea8b2203558f45fb144079a856b31dd42ed7a017ebb9504fff32474f3105c7257e4cadffd98fed2492b1c097'

    root_hex = cube_root_mod_p(y, p)

    print(root_hex)
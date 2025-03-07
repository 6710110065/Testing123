def cat_and_mouse(x: int, y: int, z: int) -> str:
    dist_a = abs(z - x)  # ระยะห่างของแมว A ถึงหนู
    dist_b = abs(z - y)  # ระยะห่างของแมว B ถึงหนู
    
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"


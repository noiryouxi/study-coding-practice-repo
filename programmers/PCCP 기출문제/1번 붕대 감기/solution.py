def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health

    time = 0
    success = 0

    for attack_time, damage in attacks:
        # 공격받기 전까지 체력 회복
        while time < attack_time - 1:
            time += 1
            health += x
            success += 1

            # t초 연속 성공하면 추가 회복
            if success == t:
                health += y
                success = 0

            # 최대 체력 제한
            health = min(health, max_health)

        # 몬스터의 공격
        time = attack_time
        health -= damage
        success = 0

        # 체력이 0 이하라면 사망
        if health <= 0:
            return -1

    return health
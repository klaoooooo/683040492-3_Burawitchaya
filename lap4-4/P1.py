import room
if __name__ == "__main__":

    #print("=== Room1 ===")
    #room1 = room.Room(10, 12)
    #print(f"Area: {room1.calculate_area()} ft")
    #print(f"Purpose: {room1.get_purpose()}")

    print("\n== Bedroom ==")
    bedroom = room.Bedroom(12, 15, 3.5)
    print(bedroom.describe_room())
    print(f"I am {bedroom.get_purpose()}")
    print(f"lighting: {bedroom.get_recommended_lighting()} lumens")

    print("\n== Kitchen1 ==")
    kitchen1 = room.Kitchen(20, 25, has_island=True)
    print(kitchen1.describe_room())
    print(f"Purpose: {kitchen1.get_purpose()}")
    print(f"Recommended lighting: {kitchen1.get_recommended_lighting()} lumens")
    island, wall = kitchen1.calculate_counter_space()
    print(f"Island counter: {island:.0f} sq ft")    
    print(f"Wall counter: {wall:.0f} sq ft")

    print("\n== Kitchen2 ==")
    kitchen2 = room.Kitchen(15, 20, has_island=False)
    print(kitchen2.describe_room())
    print(f"Recommended lighting: {kitchen2.get_recommended_lighting()} lumens")
    island_space, wall_space = kitchen2.calculate_counter_space()
    print(f"Island counter: {island_space:.0f} sq ft")    
    print(f"Wall counter: {wall_space:.0f} sq ft")
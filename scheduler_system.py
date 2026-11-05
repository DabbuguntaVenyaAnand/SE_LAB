"""Book conference rooms and equipment, and export the schedule."""

import json
from collections import Counter
from datetime import datetime
from itertools import count

reservations = {}
equipment_pool = {"projector": 2, "microphone": 4, "webcam": 1}
conflicts = []
RESERVATION_IDS = count(1)


def parse_slot(time_slot):
    """Return start and end hours for a valid HH-HH range."""
    if not isinstance(time_slot, str):
        raise ValueError("Use an hour range such as 09-11.")
    parts = time_slot.split("-")
    if len(parts) != 2 or any(
        len(part) != 2 or not part.isascii() or not part.isdigit()
        for part in parts
    ):
        raise ValueError("Use an hour range such as 09-11.")
    start, end = map(int, parts)
    if not 0 <= start < end <= 24:
        raise ValueError("Hours must satisfy 00 <= start < end <= 24.")
    return start, end


def schedule_room(room_id, time_slot, equipment_list=None):
    """Book a room only when its time and requested equipment are valid."""
    start, end = parse_slot(time_slot)
    if not isinstance(room_id, str) or not room_id.strip():
        raise ValueError("A room name is required.")
    equipment = list(equipment_list) if equipment_list is not None else []
    required = Counter(equipment)
    for name, quantity in required.items():
        if name not in equipment_pool:
            raise ValueError(f"Unknown equipment: {name}")
        if quantity > equipment_pool[name]:
            raise ValueError(f"Not enough equipment: {name}")
    for booking in reservations.values():
        booked_start, booked_end = parse_slot(booking["slot"])
        overlaps = start < booked_end and end > booked_start
        if booking["room"] == room_id and overlaps:
            message = f"{room_id} double-booked at {time_slot}"
            conflicts.append(message)
            raise ValueError(message)
    reservation_id = next(RESERVATION_IDS)
    for name, quantity in required.items():
        equipment_pool[name] -= quantity
    reservations[reservation_id] = {
        "room": room_id, "slot": time_slot, "equipment": equipment
    }
    return reservation_id


def cancel_reservation(reservation_id):
    """Release a booking's equipment; return False if the ID is unknown."""
    booking = reservations.pop(reservation_id, None)
    if booking is None:
        return False
    for name in booking["equipment"]:
        equipment_pool[name] += 1
    return True


def slot_hours(time_slot):
    """Return the duration of a validated hour range."""
    start, end = parse_slot(time_slot)
    return end - start


def export_schedule(file="schedule.json"):
    """Write reservations as UTF-8 JSON and close the file reliably."""
    with open(file, "w", encoding="utf-8") as schedule_file:
        json.dump(reservations, schedule_file, indent=2)


def log_conflicts(file="conflicts.log"):
    """Append pending conflicts and display the log using Python."""
    with open(file, "a", encoding="utf-8") as log_file:
        for conflict in conflicts:
            log_file.write(f"{datetime.now()} {conflict}\n")
    conflicts.clear()
    with open(file, "r", encoding="utf-8") as log_file:
        print(log_file.read(), end="")


def main():
    """Demonstrate booking validation and accept one interactive booking."""
    schedule_room("Board-1", "09-11")
    for room, slot in (
        ("Board-1", "09-11"), ("Huddle-3", "14-12"), ("Huddle-3", 1530)
    ):
        try:
            schedule_room(room, slot)
        except ValueError as error:
            print(f"Booking rejected: {error}")
    print("Slot length for Board-1:", slot_hours("09-11"))
    if not cancel_reservation(77):
        print("Reservation 77 was not found.")
    while True:
        slot = input("Slot for Board-2, like 10-12 (Enter for 10-12): ")
        try:
            schedule_room("Board-2", slot or "10-12", ["projector", "webcam"])
        except ValueError as error:
            print(f"Booking rejected: {error}")
        else:
            break
    export_schedule()
    log_conflicts()
    print("Equipment left:", equipment_pool)
    print("Reservations:", reservations)


if __name__ == "__main__":
    main()

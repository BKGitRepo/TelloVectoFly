#!/usr/bin/env python

from tello_sim import RealtimeSimulator

def main():
    my_drone = RealtimeSimulator()
    print("Tello Drone Simulator Ready!")
    print("Available commands: takeoff, land, forward, back, left, right, up, down, cw, ccw, flip")
    print("Special commands: save, load, exit")
    print("Type 'exit' to quit")

    while True:
        # Get command from user
        cmd = input("Enter command (e.g., 'forward 100'): ").strip().lower()
        
        if cmd == 'exit':
            break
        elif cmd.startswith('save'):
            # Handle save command
            parts = cmd.split()
            filename = parts[1] if len(parts) > 1 else "commands.json"
            my_drone.save(filename)
            continue
        elif cmd.startswith('load'):
            # Handle load command
            parts = cmd.split()
            if len(parts) < 2:
                print("Please specify a file to load (e.g., 'load my_flight.json')")
                continue
            try:
                my_drone.load_commands(parts[1])
            except FileNotFoundError:
                print(f"File {parts[1]} not found")
            continue
            
        try:
            # Parse command and distance/angle
            parts = cmd.split()
            if len(parts) == 1:
                # Commands without parameters
                if hasattr(my_drone, parts[0]):
                    getattr(my_drone, parts[0])()
            elif len(parts) == 2:
                # Commands with one parameter
                command, value = parts
                if command == 'flip':
                    getattr(my_drone, command)(value)
                else:
                    getattr(my_drone, command)(int(value))
            else:
                print("Invalid command format")
                
        except Exception as e:
            print(f"Error executing command: {e}")

if __name__ == "__main__":
    main()


# Game

Gameplay will have day and night

Once the player touches the time piece, the game will turn into "night" mode and time will start to reverse. The player must exit the level before the background music "ends"

# Level goal

Get the time piece and come back to where u started

# Tile

A tile is a small, square piece of land that cannot move. Some tiles can interact with the player

## Types
- Non-interactables
    - Wall
    - Floor (includes one way floors)
    - Piston (Basically a wall or a floor)
- Reactive to environment
    - Pressure Plate

# Tile-Entity

A tile entity can easily be thought as a "movable tile"

They can be on top of tiles. One tile can only have one entity.

## Types

- Player
- Boxes
    - Wooden boxes
    - Iron boxes
    - Slabs (movable boxes but being able to pass)
- Mechanics
    - Switch

## Recording

The grid will handle the recording part

# Entity

These are enemies that will kill you. Think like a Goomba or Koopa Troopa. Their coordinates are not integers but they have to have predictable AI. 

# Grid

The grid contains every information about the tiles and entities. It also handles the movement of the player and interactable tiles

Each tile will be `64x64`

# Movement

Use WASD or arrow keys to move the player

To move a box, just go in front of it and move (cannot push if there is a wall behind)

# Time pieces

order: bottom, top left, top right, center, bottom left, bottom right, top

## The piece of aether

The ability to extract the flow of time and store it as a fluid

## The piece of dilation

The ability to speed up and slow down the flow of time

## The piece of life

The ability to absorb the energy of the reality

## The piece of connection

The ability to combine all the pieces of time

## The piece of projection

The ability to project the flow of time into the future

## The piece of space

The ability to manipulate space-time

## The piece of augmentation

The ability to effect the entire universe with the 6 time pieces

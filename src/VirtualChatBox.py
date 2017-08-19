from mcpi import minecraft
from mcpi import block

helpPageCount = 2
playerName = "Player"
mc = minecraft.Minecraft.create()
blockDictionary = {
    "air": block.AIR,
    "stone": block.STONE,
    "grass": block.GRASS,
    "dirt": block.DIRT,
    "cobblestone": block.COBBLESTONE,
    "wood_planks": block.WOOD_PLANKS,
    "sapling": block.SAPLING,
    "bedrock": block.BEDROCK,
    "water_flowing": block.WATER_FLOWING,
    "water": block.WATER,
    "water_stationary": block.WATER_STATIONARY,
    "lava_flowing": block.LAVA_FLOWING,
    "lava": block.LAVA,
    "lava_stationary": block.LAVA_STATIONARY,
    "sand": block.SAND,
    "gravel": block.GRAVEL,
    "gold_ore": block.GOLD_ORE,
    "iron_ore": block.IRON_ORE,
    "coal_ore": block.COAL_ORE,
    "wood": block.WOOD,
    "leaves": block.LEAVES,
    "glass": block.GLASS,
    "lapis_lazuli_ore": block.LAPIS_LAZULI_ORE,
    "lapis_lazuli_block": block.LAPIS_LAZULI_BLOCK,
    "sandstone": block.SANDSTONE,
    "bed": block.BED,
    "cobweb": block.COBWEB,
    "grass_tall": block.GRASS_TALL,
    "wool": block.WOOL,
    "flower_yellow": block.FLOWER_YELLOW,
    "flower_cyan": block.FLOWER_CYAN,
    "mushroom_brown": block.MUSHROOM_BROWN,
    "mushroom_red": block.MUSHROOM_RED,
    "gold_block": block.GOLD_BLOCK,
    "iron_block": block.IRON_BLOCK,
    "stone_slab_double": block.STONE_SLAB_DOUBLE,
    "stone_slab": block.STONE_SLAB,
    "brick_block": block.BRICK_BLOCK,
    "tnt": block.TNT,
    "bookshelf": block.BOOKSHELF,
    "moss_stone": block.MOSS_STONE,
    "obsidian": block.OBSIDIAN,
    "torch": block.TORCH,
    "fire": block.FIRE,
    "stairs_wood": block.STAIRS_WOOD,
    "chest": block.CHEST,
    "diamond_ore": block.DIAMOND_ORE,
    "diamond_block": block.DIAMOND_BLOCK,
    "crafting_table": block.CRAFTING_TABLE,
    "farmland": block.FARMLAND,
    "furnace_inactive": block.FURNACE_INACTIVE,
    "furnace_active": block.FURNACE_ACTIVE,
    "door_wood": block.DOOR_WOOD,
    "ladder": block.LADDER,
    "stairs_cobblestone": block.STAIRS_COBBLESTONE,
    "door_iron": block.DOOR_IRON,
    "redstone_ore": block.REDSTONE_ORE,
    "snow": block.SNOW,
    "ice": block.ICE,
    "snow_block": block.SNOW_BLOCK,
    "cactus": block.CACTUS,
    "clay": block.CLAY,
    "sugar_cane": block.SUGAR_CANE,
    "fence": block.FENCE,
    "glowstone_block": block.GLOWSTONE_BLOCK,
    "bedrock_invisible": block.BEDROCK_INVISIBLE,
    "stone_brick": block.STONE_BRICK,
    "glass_pane": block.GLASS_PANE,
    "melon": block.MELON,
    "fence_gate": block.FENCE_GATE,
    "glowing_obsidian": block.GLOWING_OBSIDIAN,
    "nether_reactor_core": block.NETHER_REACTOR_CORE,
    "minecraft:air": block.AIR,
    "minecraft:stone": block.STONE,
    "minecraft:grass": block.GRASS,
    "minecraft:dirt": block.DIRT,
    "minecraft:cobblestone": block.COBBLESTONE,
    "minecraft:wood_planks": block.WOOD_PLANKS,
    "minecraft:sapling": block.SAPLING,
    "minecraft:bedrock": block.BEDROCK,
    "minecraft:water_flowing": block.WATER_FLOWING,
    "minecraft:water": block.WATER,
    "minecraft:water_stationary": block.WATER_STATIONARY,
    "minecraft:lava_flowing": block.LAVA_FLOWING,
    "minecraft:lava": block.LAVA,
    "minecraft:lava_stationary": block.LAVA_STATIONARY,
    "minecraft:sand": block.SAND,
    "minecraft:gravel": block.GRAVEL,
    "minecraft:gold_ore": block.GOLD_ORE,
    "minecraft:iron_ore": block.IRON_ORE,
    "minecraft:coal_ore": block.COAL_ORE,
    "minecraft:wood": block.WOOD,
    "minecraft:leaves": block.LEAVES,
    "minecraft:glass": block.GLASS,
    "minecraft:lapis_lazuli_ore": block.LAPIS_LAZULI_ORE,
    "minecraft:lapis_lazuli_block": block.LAPIS_LAZULI_BLOCK,
    "minecraft:sandstone": block.SANDSTONE,
    "minecraft:bed": block.BED,
    "minecraft:cobweb": block.COBWEB,
    "minecraft:grass_tall": block.GRASS_TALL,
    "minecraft:wool": block.WOOL,
    "minecraft:flower_yellow": block.FLOWER_YELLOW,
    "minecraft:flower_cyan": block.FLOWER_CYAN,
    "minecraft:mushroom_brown": block.MUSHROOM_BROWN,
    "minecraft:mushroom_red": block.MUSHROOM_RED,
    "minecraft:gold_block": block.GOLD_BLOCK,
    "minecraft:iron_block": block.IRON_BLOCK,
    "minecraft:stone_slab_double": block.STONE_SLAB_DOUBLE,
    "minecraft:stone_slab": block.STONE_SLAB,
    "minecraft:brick_block": block.BRICK_BLOCK,
    "minecraft:tnt": block.TNT,
    "minecraft:bookshelf": block.BOOKSHELF,
    "minecraft:moss_stone": block.MOSS_STONE,
    "minecraft:obsidian": block.OBSIDIAN,
    "minecraft:torch": block.TORCH,
    "minecraft:fire": block.FIRE,
    "minecraft:stairs_wood": block.STAIRS_WOOD,
    "minecraft:chest": block.CHEST,
    "minecraft:diamond_ore": block.DIAMOND_ORE,
    "minecraft:diamond_block": block.DIAMOND_BLOCK,
    "minecraft:crafting_table": block.CRAFTING_TABLE,
    "minecraft:farmland": block.FARMLAND,
    "minecraft:furnace_inactive": block.FURNACE_INACTIVE,
    "minecraft:furnace_active": block.FURNACE_ACTIVE,
    "minecraft:door_wood": block.DOOR_WOOD,
    "minecraft:ladder": block.LADDER,
    "minecraft:stairs_cobblestone": block.STAIRS_COBBLESTONE,
    "minecraft:door_iron": block.DOOR_IRON,
    "minecraft:redstone_ore": block.REDSTONE_ORE,
    "minecraft:snow": block.SNOW,
    "minecraft:ice": block.ICE,
    "minecraft:snow_block": block.SNOW_BLOCK,
    "minecraft:cactus": block.CACTUS,
    "minecraft:clay": block.CLAY,
    "minecraft:sugar_cane": block.SUGAR_CANE,
    "minecraft:fence": block.FENCE,
    "minecraft:glowstone_block": block.GLOWSTONE_BLOCK,
    "minecraft:bedrock_invisible": block.BEDROCK_INVISIBLE,
    "minecraft:stone_brick": block.STONE_BRICK,
    "minecraft:glass_pane": block.GLASS_PANE,
    "minecraft:melon": block.MELON,
    "minecraft:fence_gate": block.FENCE_GATE,
    "minecraft:glowing_obsidian": block.GLOWING_OBSIDIAN,
    "minecraft:nether_reactor_core": block.NETHER_REACTOR_CORE
}

def help(args):
    if not (len(args) == 1 or len(args) == 0):
        invalid()
    else:
        list = True
        if(len(args) == 0):
             page = 1
        else:
            try:
                page = int(args[0])
                if page > helpPageCount:
                    page = helpPageCount
                elif page < 1:
                    page = 1
            except ValueError:
                list = False
                if args[0] == "say":
                    print '\033[0;33;0m'
                    print "say:"
                    print "Sends a message in the chat to other players."
                    print '\033[0m'
                    print "Usage:"
                    print "- /say <message: string>"
                elif args[0] == "tp":
                    print '\033[0;33;0m'
                    print "tp:"
                    print "Teleports player."
                    print '\033[0m'
                    print "Usage:"
                    print "- /tp <destination: x y z>"
                elif args[0] == "me":
                    print '\033[0;33;0m'
                    print "me:"
                    print "Makes an action to others."
                    print '\033[0m'
                    print "Usage:"
                    print "- /me <action: string>"
                elif args[0] == "setblock":
                    print '\033[0;33;0m'
                    print "setblock:"
                    print "Changes a block to another block."
                    print '\033[0m'
                    print "Usages:"
                    print "- /setblock <position: x y z> <tileName: string> [tileData: int]"
                    print "- /setblock <position: x y z> <tileId: int> [tileData: int]"
                elif args[0] == "fill" or args[0] == "setblocks":
                    print '\033[0;33;0m'
                    print "fill(setblocks):"
                    print "Fills all of a region with a specific block."
                    print '\033[0m'
                    print "Usage:"
                    print "- /fill <from: x y z> <to: x y z> <tileName: string> [tileData: int]"
                    print "- /fill <from: x y z> <to: x y z> <tileId: int> [tileData: int]"
                elif args[0] == "help" or "?":
                    print '\033[0;33;0m'
                    print "help:"
                    print "Provides help/list of commands."
                    print '\033[0m'
                    print "Usage:"
                    print "- /help <command: string>"
                    print "- /help [page: int]"
                elif args[0] == "setplayername":
                    print '\033[0;33;0m'
                    print "setplayername:"
                    print "Changes the player's name to another name."
                    print '\033[0m'
                    print "Usage:"
                    print "- /setplayername [newPlayerName: string]"
                else:
                    print '\033[0;31;0m'
                    print "The command is defined."
                    print '\033[0m'
        if list:
            print '\033[0;32;0m'
            print "--- Showing help page " + str(page) + " of " + str(helpPageCount) + " (/help <page>) ---"
            print '\033[0m'
            if page == 1:
                print "/fill <from: x y z> <to: x y z> <tileName: string> [tileData: int]"
                print "/fill <from: x y z> <to: x y z> <tileId: int> [tileData: int]"
                print "/help <command: string>"
                print "/help [page: int]"
                print "/me <action: string>"
                print "/say <message: string>"
                print "/setblock <position: x y z> <tileName: string> [tileData: int]"
            elif page == 2:
                print "/setblock <position: x y z> <tileId: int> [tileData: int]"
                print "/setplayername [newPlayerName: string]"
                print "/tp <destination: x y z>"

def setplayername(args):
    if not (len(args) == 1 or len(args) == 0):
        invalid()
    else:
        if(len(args) == 1):
            playerName = args[0]
        else:
            playerName = "Player"
        mc.postToChat("Player's name changed successfully")


def say(args):
    if not (len(args) > 0):
        invalid()
    else:
        output = ""
        for argv in args:
            output += " " + argv
        mc.postToChat("[" + playerName + "]" + output)


def me(args):
    if not (len(args) > 0):
        invalid()
    else:
        output = ""
        for argv in args:
            output += " " + argv
        mc.postToChat("* " + playerName + output)


def teleport(args):
    if not (len(args) == 3):
        invalid()
    else:
        vec = getvec(args[0], args[1], args[2])
        if not vec:
            return
        else:
            mc.player.setTilePos(vec[0], vec[1], vec[2])
            mc.postToChat("Teleport Player to " + str(vec[0]) + ", " + str(vec[1]) + ", " + str(vec[2]))


def setblock(args):
    if not (len(args) == 4 or len(args) == 5):
        invalid()
    else:
        vec = getvec(args[0], args[1], args[2])
        if not vec:
            return
        else:
            if len(args) == 5:
                special = toint(args[4], 0, 15)
                if special == -1:
                    return
            else:
                special = 0
            if args[3] in blockDictionary.keys():
                mc.setBlock(int(vec[0]), int(vec[1]), int(vec[2]), blockDictionary[args[3]], special)
                mc.postToChat("Block placed")
            else:
                blockId = toint(args[3], 0, 256)
                if blockId == -1:
                    return
                mc.setBlock(int(vec[0]), int(vec[1]), int(vec[2]), block.Block(blockId), special)
                mc.postToChat("Block placed")


def fill(args):
    if not (len(args) == 7 or len(args) == 8):
        invalid()
    else:
        vecB = getvec(args[0], args[1], args[2])
        if vecB == False:
            return
        vecE = getvec(args[3], args[4], args[5])
        if vecE == False:
            return
        else:
            if (len(args) == 8):
                special = toint(args[7], 0, 15)
                if special == -1:
                    return
            else:
                special = 0
            if (args[6] in blockDictionary.keys()):
                mc.setBlocks(int(vecB[0]), int(vecB[1]), int(vecB[2]), int(vecE[0]), int(vecE[1]), int(vecE[2]),
                             blockDictionary[args[6]], special)
            else:
                blockId = toint(args[6], 0, 256)
                if (blockId == -1):
                    return
                mc.setBlocks(int(vecB[0]), int(vecB[1]), int(vecB[2]), int(vecE[0]), int(vecE[1]), int(vecE[2]),
                             block.Block(blockId), special)


def switchcommand(args):
    if args[0] == "say":
        say(args[1:])
    elif args[0] == "tp":
        teleport(args[1:])
    elif args[0] == "me":
        me(args[1:])
    elif args[0] == "setblock":
        setblock(args[1:])
    elif args[0] == "fill" or args[0] == "setblocks":
        fill(args[1:])
    elif args[0] == "help" or "?":
        help(args[1:])
    elif args[0] == "setplayername":
        setplayername(args[1:])
    else:
        mc.postToChat("Unknown command. Try /help for a list of commands")


def invalid():
    mc.postToChat("Invalid command syntax")


def toomin(num, min):
    mc.postToChat("The number you have entered (" + str(num) + ") is too big, it must be at most " + str(max))


def toomax(num, max):
    mc.postToChat("The number you have entered (" + str(num) + ") is too small, it must be at least " + str(max))


def toint(intStr, min, max):
    try:
        res = int(intStr)
        if res < min:
            toomin(res, min)
            return -1
        if res > max:
            toomax(res, max)
            return -1
    except ValueError:
        invalid()
        return -1


def getvec(x, y, z):
    vec = [0, 0, 0]
    if x[0] == "~":
        try:
            if len(x) == 1:
                add = 0
            else:
                add = float(x[1:])
        except ValueError:
            invalid()
            return False
        vec[0] = mc.player.getTilePos().x + add
    else:
        try:
            vec[0] = float(x)
        except ValueError:
            invalid()
            return False
    if y[0] == "~":
        try:
            if len(y) == 1:
                add = 0
            else:
                add = float(y[1:])
        except ValueError:
            invalid()
            return False
        vec[1] = mc.player.getTilePos().y + add
    else:
        try:
            vec[1] = float(y)
        except ValueError:
            invalid()
            return False
    if z[0] == "~":
        try:
            if len(z) == 1:
                add = 0
            else:
                add = float(z[1:])
        except ValueError:
            invalid()
            return False
        vec[2] = mc.player.getTilePos().z + add
    else:
        try:
            vec[2] = float(z)
        except ValueError:
            invalid()
            return False
    return vec


while True:
    input = raw_input("> ")
    if input == '\x1b':
        break
    if len(input) == 0:
        continue
    if not (input.find("/") == 0):
        mc.postToChat("<" + playerName + "> " + input)
        continue
    args = []
    argv = ""
    for word in input[1:] + " ":
        if not (word == " "):
            argv += word
        else:
            args.append(argv)
            argv = ""
    switchcommand(args)

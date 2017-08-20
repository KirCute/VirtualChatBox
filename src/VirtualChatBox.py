import os
import socket
import sys
import time
import threading
from mcpi import minecraft, block, vec3

disablems = False
try:
    import minecraftstuff
except ImportError:
    print '\033[0;33;40m',
    print "Warning: Package \"minecraftstuff\" is defined."
    print " It means some commands will not be available."
    print " Try \"sudo pip install minecraftstuff\" to get it.",
    print '\033[0m'
    disablems = True

try:
    global mc
    if len(sys.argv) == 3:
        mc = minecraft.Minecraft.create(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) == 2:
        mc = minecraft.Minecraft.create(sys.argv[1])
    elif len(sys.argv) == 1:
        mc = minecraft.Minecraft.create()
    else:
        raise TypeError("parameters are too many.")
except ValueError:
    print '\033[0;31;40m',
    print "Parameter value error: ", sys.exc_info()[1],
    print '\033[0m'
    sys.exit(1)
except TypeError:
    print '\033[0;31;40m',
    print "Parameter type error: ", sys.exc_info()[1],
    print '\033[0m'
    sys.exit(1)
except socket.error, arg:
    (errno, err_msg) = arg
    print '\033[0;31;40m',
    print "Cannot connect to server: %s, errno=%d" % (err_msg, errno),
    print '\033[0m'
    sys.exit(1)
if not disablems:
    mcdraw = minecraftstuff.MinecraftDrawing(mc)
    mcshapes = {}
    mcturtles = {}
threads = {}
helpPageCount = 4
playerName = "Player"
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


def tocommand(args):
    command = merge(args)
    if command[1] == "/":
        command = command[2:]
    else:
        command = command[1:]
    return command


def thread(args, super):
    if len(args) == 0:
        invalid(super)
    elif args[0] == "add":
        if len(args) < 4:
            invalid(super)
            return
        name = args[1]
        if len(name) == 0:
            invalid(super)
            return
        if len(name) > 15:
            if super is None:
                print '\033[0;31;40m',
                print "The name you have entered (" + name + ") is too long, it must be at longest 15",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("The name you have entered (" + name + ") is too long, it must be at longest 15", super)
            return
        if name in threads.keys():
            if super is None:
                print '\033[0;31;40m',
                print "Thread " + name + " already exists.",
                print '\033[0m'
                return
            trystop(super)
            chatWithSuper("Thread " + name + " already exists.", super)
            return
        sleep = toint(args[2], 0, 2147483647, super)
        if sleep <= -1:
            return
        command = tocommand(args[3:])
        if super is None:
            threads[name] = CommandThread("t_" + name, command, float(sleep / 20))
        else:
            threads[name] = CommandThread(super + ".t_" + name, command, float(sleep / 20))
        threads[name].start()
        chatWithSuper("Created Thread " + name + " successfully.", super)
    elif args[0] == "start":
        if not len(args) == 2:
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        chatWithSuper("Thread " + name + " is running now.", super)
        threads[name].continuethread()
    elif args[0] == "stop":
        if not len(args) == 2:
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        threads[name].setpause()
        chatWithSuper("Thread " + name + " is stoped.", super)
    elif args[0] == "remove":
        if not len(args) == 2:
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        threads[name].stop()
        del threads[name]
        chatWithSuper("Removed Thread " + name + ".", super)
    elif args[0] == "list":
        if not (super is None):
            trystop(super)
            chatWithSuper("Cannot use /thread list in a function or a thread.", super)
            return
        print '\033[0;32;40m', "-------- Showing list of threads --------"
        print " Thread Name     Status", '\033[0m'
        for threadname in threads.keys():
            print " " + threadname.ljust(15),
            if threads[threadname].ispause():
                print "Stoped"
            else:
                print "Running"
    elif args[0] == "clear":
        for name in threads.keys():
            threads[name].stop()
            del threads[name]
        chatWithSuper("Cleared threads.", super)
    elif args[0] == "setsleep":
        if not (len(args) == 3):
            invalid(super)
            return
        name = args[1]
        if not (name in threads.keys()):
            chatWithSuper("Thread " + name + " doesn't exists.", super)
            return
        sleep = toint(args[2], 0, 2147483647, super)
        if sleep <= -1:
            return
        threads[name].setsleep(float(sleep / 20))
    else:
        invalid(super)


def superoutput(super):
    if "." in super:
        threadname = super[2:super.find(".") + 1]
        fun = superoutput(super[find(".") + 1:])
        return threadname + "." + fun
    else:
        return super[2:]


def trystop(super):
    super = super + "."
    if "t_" in super:
        threads[super[super.rfind("t_") + 2 : super.find(".", super.rfind("t_"))]].setpause()


def chatWithSuper(msg, super):
    if super is None:
        mc.postToChat(msg)
    else:
        mc.postToChat("[" + superoutput(super) + "] " + msg)


class CommandThread(threading.Thread):
    def __init__(self, name, command, sleep):
        threading.Thread.__init__(self)
        self.name = name
        self.command = command
        self.sleep = sleep
        self.pause = True
        self.delete = False

    def run(self):
        while not self.delete:
            if not self.pause:
                readCommand(self.command, self.name)
                time.sleep(self.sleep)

    def continuethread(self):
        self.pause = False

    def setpause(self):
        self.pause = True

    def setsleep(self, sleep):
        self.sleep = sleep

    def ispause(self):
        return self.pause

    def stop(self):
        self.delete = True


def draw(args, super):
    if disablems:
        if not (super is None):
            trystop(super)
            chatWithSuper("Package \"minecraftstuff\" is defined, \"/draw\" is not available.", super)
            return
        print '\033[0;33;40m',
        print "Package \"minecraftstuff\" is defined, \"/draw\" is not available.",
        print '\033[0m'
        return
    if len(args) == 0:
        invalid(super)
        return
    if args[0] == "circle":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawCircle(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew circle successfully.", super)
    elif args[0] == "face":
        blocklist = []
        if len(args) >= 7 and not ((len(args) - 4) % 3):
            filled = tobool(args[-3], super)
            if filled <= -1:
                return
            block = getblock(args[-2], super)
            if block <= -1:
                return
            special = toint(args[-1], 0, 15, super)
            if special <= -1:
                return
            times = (len(args) - 4) / 3
        elif len(args) >= 6 and not ((len(args) - 3) % 3):
            filled = tobool(args[-2], super)
            if filled <= -1:
                return
            block = getblock(args[-1], super)
            if block <= -1:
                return
            special = 0
            times = (len(args) - 3) / 3
        else:
            invalid(super)
            return
        time = 1
        while time <= times:
            veclist = getvec(args[time * 3 - 2], args[time * 3 - 1], args[time * 3], False, super)
            if not veclist:
                return
            blocklist.append(vec3.Vec3(veclist[0], veclist[1], veclist[2]))
            time += 1
        mcdraw.drawFace(blocklist, filled, block, special)
        chatWithSuper("Drew face successfully.", super)
    elif args[0] == "hollowSphere":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawHollowSphere(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew hollow sphere successfully.", super)
    elif args[0] == "horizontalCircle":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawHorizontalCircle(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew circle successfully.", super)
    elif args[0] == "line":
        if not (len(args) == 8 or len(args) == 9):
            invalid(super)
            return
        vecB = getvec(args[1], args[2], args[3], False, super)
        if not vecB:
            return
        vecE = getvec(args[4], args[5], args[6], False, super)
        if not vecE:
            return
        block = getblock(args[7], super)
        if block <= -1:
            return
        if len(args) == 9:
            special = toint(args[8], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawLine(vecB[0], vecB[1], vecB[2], vecE[0], vecE[1], vecE[2], block, special)
        chatWithSuper("Drew line successfully.", super)
    elif args[0] == "point":
        if not (len(args) == 5 or len(args) == 6):
            invalid(super)
        else:
            vec = getvec(args[1], args[2], args[3], False, super)
            if not vec:
                return
            else:
                if len(args) == 6:
                    special = toint(args[5], 0, 15, super)
                    if special <= -1:
                        return
                else:
                    special = 0
                block = getblock(args[4], super)
                if block <= -1:
                    return
                mc.setBlock(vec[0], vec[1], vec[2], block, special)
                chatWithSuper("Drew point successfully.", super)
    elif args[0] == "sphere":
        if not (len(args) == 6 or len(args) == 7):
            invalid(super)
            return
        vec = getvec(args[1], args[2], args[3], False, super)
        radius = toint(args[4], 0, 64, super)
        if radius <= -1:
            return
        block = getblock(args[5], super)
        if block <= -1:
            return
        if len(args) == 7:
            special = toint(args[4], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        mcdraw.drawSphere(vec[0], vec[1], vec[2], radius, block, special)
        chatWithSuper("Drew sphere successfully.", super)
    elif args[0] == "vertices":
        blocklist = []
        if len(args) >= 6 and not ((len(args) - 3) % 3):
            block = getblock(args[-2], super)
            if block <= -1:
                return
            special = toint(args[-1], 0, 15, super)
            if special <= -1:
                return
            times = (len(args) - 3) / 3
        elif len(args) >= 5 and not ((len(args) - 2) % 3):
            block = getblock(args[-1], super)
            if block <= -1:
                return
            special = 0
            times = (len(args) - 2) / 3
        else:
            invalid(super)
            return
        time = 1
        while time <= times:
            veclist = getvec(args[time * 3 - 2], args[time * 3 - 1], args[time * 3], False, super)
            if not veclist:
                return
            blocklist.append(vec3.Vec3(veclist[0], veclist[1], veclist[2]))
            time += 1
        mcdraw.drawVertices(blocklist, block, special)
        chatWithSuper("Drew vertices successfully.", super)
    else:
        invalid(super)


def setting(args, super):
    if not (len(args) == 0 or len(args) == 2):
        invalid(super)
    else:
        if len(args) == 0:
            if super is None:
                print "autojump, nametags_visible, world_immutable"
            else:
                trystop(super)
                chatWithSuper("Cannot use /setting in a function or a thread.", super)
                return
        else:
            setting = tobool(args[1], super)
            if setting <= -1:
                return
            if args[0] == "autojump":
                mc.player.setting("autojump", setting)
            elif args[0] == "nametags_visible":
                mc.setting("nametags_visible", setting)
            elif args[0] == "world_immutable":
                mc.setting("world_immutable", setting)
            else:
                invalid(super)
                return
            chatWithSuper("Changed the " + args[0] + " setting to " + args[1], super)


def clear(args, super):
    if not (super is None):
        trystop(super)
        chatWithSuper("Cannot use /clear in a function or a thread.", super)
        return
    if not (len(args) == 0):
        invalid(None)
    else:
        os.system("clear")


def help(args, super):
    if not (super is None):
        trystop(super)
        chatWithSuper("Cannot use /help in a function or a thread.", super)
        return
    if not (len(args) == 1 or len(args) == 0):
        invalid(None)
    else:
        list = True
        try:
            if len(args) == 0:
                page = 1
            else:
                page = int(args[0])
            if page > helpPageCount:
                page = helpPageCount
            elif page < 1:
                page = 1
        except ValueError:
            list = False
            if args[0] == "say":
                print '\033[0;33;40m',
                print "say:"
                print " Sends a message in the chat to other players."
                print '\033[0m',
                print "Usage:"
                print " - /say <message: string>"
            elif args[0] == "tp":
                print '\033[0;33;40m',
                print "tp:"
                print " Teleports player."
                print '\033[0m',
                print "Usage:"
                print " - /tp <destination: x y z>"
            elif args[0] == "me":
                print '\033[0;33;40m',
                print "me:"
                print " Makes an action to others."
                print '\033[0m',
                print "Usage:"
                print " - /me <action: string>"
            elif args[0] == "setblock":
                print '\033[0;33;40m',
                print "setblock:"
                print " Changes a block to another block."
                print '\033[0m',
                print "Usages:"
                print " - /setblock <position: x y z> <tileName: string> [tileData: int]"
                print " - /setblock <position: x y z> <tileId: int> [tileData: int]"
            elif args[0] == "fill" or args[0] == "setblocks":
                print '\033[0;33;40m',
                print "fill(setblocks):"
                print " Fills all of a region with a specific block."
                print '\033[0m',
                print "Usage:"
                print " - /fill <from: x y z> <to: x y z> <tileName: string> [tileData: int]"
                print " - /fill <from: x y z> <to: x y z> <tileId: int> [tileData: int]"
            elif args[0] == "help":
                print '\033[0;33;40m',
                print "help:"
                print " Provides help/list of commands."
                print '\033[0m',
                print "Usage:"
                print " - /help <command: string>"
                print " - /help [page: int]"
            elif args[0] == "setplayername":
                print '\033[0;33;40m',
                print "setplayername:"
                print " Changes the player's name to another name."
                print '\033[0m',
                print "Usage:"
                print " - /setplayername [newPlayerName: string]"
            elif args[0] == "clear":
                print '\033[0;33;40m',
                print "clear:"
                print " Clears the screen of terminal."
                print '\033[0m',
                print "Usage:"
                print " - /clear"
            elif args[0] == "setting":
                print '\033[0;33;40m',
                print "setting:"
                print " Set a setting."
                print '\033[0m',
                print "Usage:"
                print " - /setting"
                print " - /setting <setting: string> <status: boolean>"
            elif args[0] == "draw":
                print '\033[0;33;40m',
                print "draw:"
                print " Draws some shapes made of blocks."
                if disablems:
                    print '\033[0;33;40m', "Tip: this command is now unavailable."
                print '\033[0m',
                print "Usage:"
                print " - /draw circle <position: x0 y0 z> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw face <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <filled: boolean> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw hollowSphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw horizontalCircle <position: x0 y z0> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw line <position1: x1 y1 z1> <position2: x2 y2 z2> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw point <position: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw sphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]"
                print " - /draw vertices <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <tileName: string | tileId: int> [tileData: int]"
            elif args[0] == "thread":
                print '\033[0;33;40m',
                print "thread:"
                print " Manages threads to do something looped in cycles."
                print '\033[0m',
                print "Usage:"
                print " - /thread add <threadName: string> <sleepTime: int> <command: stirng>"
                print " - /thread clear"
                print " - /thread list"
                print " - /thread remove <threadName: string>"
                print " - /thread setsleep <threadName: string> <sleepTime: int>"
                print " - /thread start <threadName: string>"
                print " - /thread stop <threadName: string>"
            else:
                print '\033[0;31;40m',
                print "The command is defined.",
                print '\033[0m'
        if list:
            print '\033[0;32;40m',
            print "--- Showing help page " + str(page) + " of " + str(helpPageCount) + " (/help <page>) ---"
            if page == 1:
                print '\033[0m', "/clear"
                print " /fill <from: x y z> <to: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " /help [command: string | page: int]"
                print " /me <action: string>"
                print " /say <message: string>"
                print " /setblock <position: x y z> <tileName: string | tileId: int> [tileData: int]"
                print " /setplayername [newPlayerName: string]"
            elif page == 2:
                print '\033[0m', "/setting [<setting: string> <status: boolean>]"
                print " /thread add <threadName: string> <sleepTime: int> <command: stirng>"
                print " /thread clear"
                print " /thread list"
                print " /thread remove <threadName: string>"
                print " /thread setsleep <threadName: string> <sleepTime: int>"
                print " /thread start <threadName: string>"
            elif page == 3:
                print " /thread stop <threadName: string>"
                print " /tp <destination: x y z>"
                print '\033[0;33;40m', "/draw circle <position: x0 y0 z> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw face <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <filled: boolean> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw hollowSphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw horizontalCircle <position: x0 y z0> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw line <position1: x1 y1 z1> <position2: x2 y2 z2> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
            elif page == 4:
                print '\033[0;33;40m', "/draw point <position: x y z> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw sphere <position: x y z> <radius: int> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
                print '\033[0;33;40m', "/draw vertices <<position1: x1 y1 z1> [position2: x2 y2 z2] [position3: x3 y3 z3] ...> <tileName: string | tileId: int> [tileData: int]", '\033[0m'
            print '\033[0;32;40m', "Tip:", '\033[0;33;40m', "yellow", '\033[0;32;40m', "commands are add-ons' commands.", '\033[0m'


def setplayername(args, super):
    if not (len(args) == 1 or len(args) == 0):
        invalid(super)
    else:
        global playerName
        if len(args) == 1:
            playerName = args[0]
            if len(playerName) == 0:
                invalid(super)
                return
        else:
            playerName = "Player"
        chatWithSuper("Player's name changed to \"" + playerName + "\" successfully", super)


def merge(args):
    output = ""
    for argv in args:
        output += " " + argv
    return output


def say(args, super):
    if not (len(args) > 0):
        invalid(super)
    else:
        output = merge(args)
        if super is None:
            mc.postToChat("[" + playerName + "]" + output)
        else:
            chatWithSuper(output, super)


def me(args, super):
    if not (len(args) > 0):
        invalid(super)
    else:
        output = merge(args)
        if super is None:
            mc.postToChat("* " + playerName + output)
        else:
            mc.postToChat("* " + superoutput(super) + output)


def teleport(args, super):
    if not (len(args) == 3):
        invalid(super)
    else:
        vec = getvec(args[0], args[1], args[2], True, super)
        if not vec:
            return
        else:
            mc.player.setTilePos(vec[0], vec[1], vec[2])
            chatWithSuper("Teleport Player to " + str(vec[0]) + ", " + str(vec[1]) + ", " + str(vec[2]), super)


def setblock(args, super):
    if not (len(args) == 4 or len(args) == 5):
        invalid(super)
    else:
        vec = getvec(args[0], args[1], args[2], False, super)
        if not vec:
            return
        else:
            if len(args) == 5:
                special = toint(args[4], 0, 15, super)
                if special <= -1:
                    return
            else:
                special = 0
            block = getblock(args[3], super)
            if block <= -1:
                return
            mc.setBlock(vec[0], vec[1], vec[2], block, special)
            chatWithSuper("Block placed", super)


def fill(args, super):
    if not (len(args) == 7 or len(args) == 8):
        invalid(super)
    else:
        vecB = getvec(args[0], args[1], args[2], False, super)
        if not vecB:
            return
        vecE = getvec(args[3], args[4], args[5], False, super)
        if not vecE:
            return
        blockCount = (abs(vecB[0] - vecE[0]) + 1) * (abs(vecB[1] - vecE[1]) + 1) * (abs(vecB[2] - vecE[2]) + 1)
        if len(args) == 8:
            special = toint(args[7], 0, 15, super)
            if special <= -1:
                return
        else:
            special = 0
        block = getblock(args[6], super)
        if block <= -1:
            return
        mc.setBlocks(vecB[0], vecB[1], vecB[2], vecE[0], vecE[1], vecE[2], block, special)
        chatWithSuper(str(blockCount) + " blocks filled", super)


def switchcommand(args, super):
    if args[0] == "say":
        say(args[1:], super)
    elif args[0] == "tp":
        teleport(args[1:], super)
    elif args[0] == "me":
        me(args[1:], super)
    elif args[0] == "setblock":
        setblock(args[1:], super)
    elif args[0] == "fill" or args[0] == "setblocks":
        fill(args[1:], super)
    elif args[0] == "help":
        help(args[1:], super)
    elif args[0] == "setplayername":
        setplayername(args[1:], super)
    elif args[0] == "clear":
        clear(args[1:], super)
    elif args[0] == "setting":
        setting(args[1:], super)
    elif args[0] == "draw":
        draw(args[1:], super)
    elif args[0] == "thread":
        thread(args[1:], super)
    else:
        if super is None:
            print '\033[0;31;40m',
            print "Unknown command. Try /help for a list of commands",
            print '\033[0m'
        else:
            trystop(super)
            chatWithSuper("Unknown command.", super)


def invalid(super):
    if super is None:
        print '\033[0;31;40m',
        print "Invalid command syntax",
        print '\033[0m'
    else:
        trystop(super)
        chatWithSuper("Invalid command syntax",super)


def toomin(num, min, super):
    if super is None:
        print '\033[0;31;40m',
        print "The number you have entered (" + str(num) + ") is too small, it must be at least " + str(min),
        print '\033[0m'
    else:
        trystop(super)
        chatWithSuper("The number you have entered (" + str(num) + ") is too small, it must be at least " + str(min), super)


def toomax(num, max, super):
    if super is None:
        print '\033[0;31;40m',
        print "The number you have entered (" + str(num) + ") is too big, it must be at most " + str(max),
        print '\033[0m'
    else:
        trystop(super)
        chatWithSuper("The number you have entered (" + str(num) + ") is too big, it must be at most " + str(max), super)


def getblock(argv, super):
    if argv in blockDictionary.keys():
        return blockDictionary[argv]
    else:
        blockId = toint(argv, 0, 256, super)
        if blockId <= -1:
            return -1


def toint(intStr, min, max, super):
    try:
        res = int(intStr)
        if res < min:
            toomin(res, min, super)
            return -1
        if res > max:
            toomax(res, max, super)
            return -1
    except ValueError:
        invalid(super)
        return -1
    return res


def tobool(argv, super):
    if argv == "true":
        return True
    elif argv == "false":
        return False
    else:
        invalid(super)
        return -1


def getvec(x, y, z, isFloat, super):
    if isFloat:
        vec = [0, 0, 0]
        if x[0] == "~":
            try:
                if len(x) == 1:
                    add = 0
                else:
                    add = float(x[1:])
            except ValueError:
                invalid(super)
                return False
            vec[0] = mc.player.getTilePos().x + add
        else:
            try:
                vec[0] = float(x)
            except ValueError:
                invalid(super)
                return False
        if y[0] == "~":
            try:
                if len(y) == 1:
                    add = 0
                else:
                    add = float(y[1:])
            except ValueError:
                invalid(super)
                return False
            vec[1] = mc.player.getTilePos().y + add
        else:
            try:
                vec[1] = float(y)
            except ValueError:
                invalid(super)
                return False
        if z[0] == "~":
            try:
                if len(z) == 1:
                    add = 0
                else:
                    add = float(z[1:])
            except ValueError:
                invalid(super)
                return False
            vec[2] = mc.player.getTilePos().z + add
        else:
            try:
                vec[2] = float(z)
            except ValueError:
                invalid(super)
                return False
    else:
        vec = [0, 0, 0]
        if x[0] == "~":
            try:
                if len(x) == 1:
                    add = 0
                else:
                    add = int(x[1:])
            except ValueError:
                invalid(super)
                return False
            vec[0] = int(mc.player.getTilePos().x) + add
        else:
            try:
                vec[0] = int(x)
            except ValueError:
                invalid(super)
                return False
        if y[0] == "~":
            try:
                if len(y) == 1:
                    add = 0
                else:
                    add = int(y[1:])
            except ValueError:
                invalid(super)
                return False
            vec[1] = int(mc.player.getTilePos().y) + add
        else:
            try:
                vec[1] = int(y)
            except ValueError:
                invalid(super)
                return False
        if z[0] == "~":
            try:
                if len(z) == 1:
                    add = 0
                else:
                    add = int(z[1:])
            except ValueError:
                invalid(super)
                return False
            vec[2] = int(mc.player.getTilePos().z) + add
        else:
            try:
                vec[2] = int(z)
            except ValueError:
                invalid(super)
                return False
    if vec[0] > 128:
        toomax(vec[0], 128, super)
    elif vec[0] < -128:
        toomin(vec[0], -128, super)
    elif vec[1] > 64:
        toomax(vec[1], 64, super)
    elif vec[1] < -64:
        toomin(vec[1], -64, super)
    elif vec[2] > 128:
        toomax(vec[2], 128, super)
    elif vec[2] < -128:
        toomin(vec[2], -128, super)
    else:
        return vec
    return False


def readCommand(command, super=None):
    commandArgs = []
    addingArgv = ""
    for word in command + " ":
        if not (word == " "):
            addingArgv += word
        else:
            commandArgs.append(addingArgv)
            addingArgv = ""
    switchcommand(commandArgs, super)


while True:
    input = raw_input("> ")
    if input == '\x1b':
        for name in threads:
            threads[name].stop()
        break
    if len(input) == 0:
        continue
    if not (input.find("/") == 0):
        mc.postToChat("<" + playerName + "> " + input)
    else:
        readCommand(input[1:])

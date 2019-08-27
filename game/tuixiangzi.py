#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 15:23
# software: PyCharm
1.  # Star Pusher (a Sokoban clone)

2.  # By Al Sweigart al@inventwithpython.com

3.  # http://inventwithpython.com/pygame

4.  # Creative Commons BY-NC-SA 3.0 US

5.

6.
import random, sys, copy, os, pygame

7.
from pygame.locals import *

8.

9.
FPS = 30  # frames per second to update the screen

10.
WINWIDTH = 800  # width of the program's window, in pixels

11.
WINHEIGHT = 600  # height in pixels

12.
HALF_WINWIDTH = int(WINWIDTH / 2)

13.
HALF_WINHEIGHT = int(WINHEIGHT / 2)

14.

15.  # The total width and height of each tile in pixels.

16.
TILEWIDTH = 50

17.
TILEHEIGHT = 85

18.
TILEFLOORHEIGHT = 45

19.

20.
CAM_MOVE_SPEED = 5  # how many pixels per frame the camera moves

21.

22.  # The percentage of outdoor tiles that have additional

23.  # decoration on them, such as a tree or rock.

24.
OUTSIDE_DECORATION_PCT = 20

25.

26.
BRIGHTBLUE = (0, 170, 255)

27.
WHITE = (255, 255, 255)

28.
BGCOLOR = BRIGHTBLUE

29.
TEXTCOLOR = WHITE

30.

31.
UP = 'up'

32.
DOWN = 'down'

33.
LEFT = 'left'

34.
RIGHT = 'right'

35.

36.

37.


def main():


38.
global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

39.

40.  # Pygame initialization and basic set up of the global variables.

41.
pygame.init()

42.
FPSCLOCK = pygame.time.Clock()

43.

44.  # Because the Surface object stored in DISPLAYSURF was returned

45.  # from the pygame.display.set_mode() function, this is the

46.  # Surface object that is drawn to the actual computer screen

47.  # when pygame.display.update() is called.

48.
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

49.

50.
pygame.display.set_caption('Star Pusher')

51.
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

52.

53.  # A global dict value that will contain all the Pygame

54.  # Surface objects returned by pygame.image.load().

55.
IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),

              56.                   'covered goal': pygame.image.load('Selector.png'),

                                                    57.
'star': pygame.image.load('Star.png'),

58.
'corner': pygame.image.load('Wall Block Tall.png'),

59.
'wall': pygame.image.load('Wood Block Tall.png'),

60.
'inside floor': pygame.image.load('Plain Block.png'),

61.
'outside floor': pygame.image.load('Grass Block.png'),

62.
'title': pygame.image.load('star_title.png'),

63.
'solved': pygame.image.load('star_solved.png'),

64.
'princess': pygame.image.load('princess.png'),

65.
'boy': pygame.image.load('boy.png'),

66.
'catgirl': pygame.image.load('catgirl.png'),

67.
'horngirl': pygame.image.load('horngirl.png'),

68.
'pinkgirl': pygame.image.load('pinkgirl.png'),

69.
'rock': pygame.image.load('Rock.png'),

70.
'short tree': pygame.image.load('Tree_Short.png'),

71.
'tall tree': pygame.image.load('Tree_Tall.png'),

72.
'ugly tree': pygame.image.load('Tree_Ugly.png')}

73.

74.  # These dict values are global, and map the character that appears

75.  # in the level file to the Surface object it represents.

76.
TILEMAPPING = {'x': IMAGESDICT['corner'],

               77.                    '#': IMAGESDICT['wall'],

                                           78.
'o': IMAGESDICT['inside floor'],

79.
' ': IMAGESDICT['outside floor']}

80.
OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],

                      81.                           '2': IMAGESDICT['short tree'],

                                                         82.
'3': IMAGESDICT['tall tree'],

83.
'4': IMAGESDICT['ugly tree']}

84.

85.  # PLAYERIMAGES is a list of all possible characters the player can be.

86.  # currentImage is the index of the player's current player image.

87.
currentImage = 0

88.
PLAYERIMAGES = [IMAGESDICT['princess'],

                89.                     IMAGESDICT['boy'],

                90.                     IMAGESDICT['catgirl'],

                91.                     IMAGESDICT['horngirl'],

                92.                     IMAGESDICT['pinkgirl']]

93.

94.
startScreen()  # show the title screen until the user presses a key

95.

96.  # Read in the levels from the text file. See the readLevelsFile() for

97.  # details on the format of this file and how to make your own levels.

98.
levels = readLevelsFile('starPusherLevels.txt')

99.
currentLevelIndex = 0

100.

101.  # The main game loop. This loop runs a single level, when the user

102.  # finishes that level, the next/previous level is loaded.

103.
while True:  # main game loop

104.  # Run the level to actually start playing the game:

105.
result = runLevel(levels, currentLevelIndex)

106.

107.
if result in ('solved', 'next'):

108.  # Go to the next level.

109.
currentLevelIndex += 1

110.
if currentLevelIndex >= len(levels):

111.  # If there are no more levels, go back to the first one.

112.
currentLevelIndex = 0

113. elif result == 'back':

114.  # Go to the previous level.

115.
currentLevelIndex -= 1

116.
if currentLevelIndex < 0:

117.  # If there are no previous levels, go to the last one.

118.
currentLevelIndex = len(levels) - 1

119. elif result == 'reset':

120.
pass  # Do nothing. Loop re-calls runLevel() to reset the level

121.

122.

123.


def runLevel(levels, levelNum):


124.
global currentImage

125.
levelObj = levels[levelnum]

126.
mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])

127.
gameStateObj = copy.deepcopy(levelObj['startState'])

128.
mapNeedsRedraw = True  # set to True to call drawMap()

129.
levelSurf = BASICFONT.render('Level %s of %s' % (levelObj['levelNum'] + 1, totalNumOfLevels), 1, TEXTCOLOR)

130.
levelRect = levelSurf.get_rect()

131.
levelRect.bottomleft = (20, WINHEIGHT - 35)

132.
mapWidth = len(mapObj) * TILEWIDTH

133.
mapHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT

134.
MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH

135.
MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT

136.

137.
levelIsComplete = False

138.  # Track how much the camera has moved:

139.
cameraOffsetX = 0

140.
cameraOffsetY = 0

141.  # Track if the keys to move the camera are being held down:

142.
cameraUp = False

143.
cameraDown = False

144.
cameraLeft = False

145.
cameraRight = False

146.

147.
while True:  # main game loop

148.  # Reset these variables:

149.
playerMoveTo = None

150.
keyPressed = False

151.

152.
for event in pygame.event.get():  # event handling loop

153.
if event.type == QUIT:

154.  # Player clicked the "X" at the corner of the window.

155.
terminate()

156.

157. elif event.type == KEYDOWN:

158.  # Handle key presses

159.
keyPressed = True

160.
if event.key == K_LEFT:

161.
playerMoveTo = LEFT

162. elif event.key == K_RIGHT:

163.
playerMoveTo = RIGHT

164. elif event.key == K_UP:

165.
playerMoveTo = UP

166. elif event.key == K_DOWN:

167.
playerMoveTo = DOWN

168.

169.  # Set the camera move mode.

170. elif event.key == K_a:

171.
cameraLeft = True

172. elif event.key == K_d:

173.
cameraRight = True

174. elif event.key == K_w:

175.
cameraUp = True

176. elif event.key == K_s:

177.
cameraDown = True

178.

179. elif event.key == K_n:

180.
return 'next'

181. elif event.key == K_b:

182.
return 'back'

183.

184. elif event.key == K_ESCAPE:

185.
terminate()  # Esc key quits.

186. elif event.key == K_BACKSPACE:

187.
return 'reset'  # Reset the level.

188. elif event.key == K_p:

189.  # Change the player image to the next one.

190.
currentImage += 1

191.
if currentImage >= len(PLAYERIMAGES):

192.  # After the last player image, use the first one.

193.
currentImage = 0

194.
mapNeedsRedraw = True

195.

196. elif event.type == KEYUP:

197.  # Unset the camera move mode.

198.
if event.key == K_a:

199.
cameraLeft = False

200. elif event.key == K_d:

201.
cameraRight = False

202. elif event.key == K_w:

203.
cameraUp = False

204. elif event.key == K_s:

205.
cameraDown = False

206.

207.
if playerMoveTo != None and not levelIsComplete:

208.  # If the player pushed a key to move, make the move

209.  # (if possible) and push any stars that are pushable.

210.
moved = makeMove(mapObj, gameStateObj, playerMoveTo)

211.

212.
if moved:

213.  # increment the step counter.

214.
gameStateObj['stepCounter'] += 1

215.
mapNeedsRedraw = True

216.

217.
if isLevelFinished(levelObj, gameStateObj):

218.  # level is solved, we should show the "Solved!" image.

219.
levelIsComplete = True

220.
keyPressed = False

221.

222.
DISPLAYSURF.fill(BGCOLOR)

223.

224.
if mapNeedsRedraw:

225.
mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])

226.
mapNeedsRedraw = False

227.

228.
if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:

229.
cameraOffsetY += CAM_MOVE_SPEED

230. elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:

231.
cameraOffsetY -= CAM_MOVE_SPEED

232.
if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:

233.
cameraOffsetX += CAM_MOVE_SPEED

234. elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:

235.
cameraOffsetX -= CAM_MOVE_SPEED

236.

237.  # Adjust mapSurf's Rect object based on the camera offset.

238.
mapSurfRect = mapSurf.get_rect()

239.
mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)

240.

241.  # Draw mapSurf to the DISPLAYSURF Surface object.

242.
DISPLAYSURF.blit(mapSurf, mapSurfRect)

243.

244.
DISPLAYSURF.blit(levelSurf, levelRect)

245.
stepSurf = BASICFONT.render('Steps: %s' % (gameStateObj['stepCounter']), 1, TEXTCOLOR)

246.
stepRect = stepSurf.get_rect()

247.
stepRect.bottomleft = (20, WINHEIGHT - 10)

248.
DISPLAYSURF.blit(stepSurf, stepRect)

249.

250.
if levelIsComplete:

251.  # is solved, show the "Solved!" image until the player

252.  # has pressed a key.

253.
solvedRect = IMAGESDICT['solved'].get_rect()

254.
solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

255.
DISPLAYSURF.blit(IMAGESDICT['solved'], solvedRect)

256.

257.
if keyPressed:

258.
return 'solved'

259.

260.
pygame.display.update()  # draw DISPLAYSURF to the screen.

261.
FPSCLOCK.tick()

262.

263.

274.


def decorateMap(mapObj, startxy):


275.
"""Makes a copy of the given map object and modifies it.

276.     Here is what is done to it:

277.         * Walls that are corners are turned into corner pieces.

278.         * The outside/inside floor tile distinction is made.

279.         * Tree/rock decorations are randomly added to the outside tiles.

280.

281.     Returns the decorated map object."""

282.

283.
startx, starty = startxy  # Syntactic sugar

284.

285.  # Copy the map object so we don't modify the original passed

286.
mapObjCopy = copy.deepcopy(mapObj)

287.

288.  # Remove the non-wall characters from the map data

289.
for x in range(len(mapObjCopy)):

290.
for y in range(len(mapObjCopy[0])):

291.
if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):

292.
mapObjCopy[x][y] = ' '

293.

294.  # Flood fill to determine inside/outside floor tiles.

295.
floodFill(mapObjCopy, startx, starty, ' ', 'o')

296.

297.  # Convert the adjoined walls into corner tiles.

298.
for x in range(len(mapObjCopy)):

299.
for y in range(len(mapObjCopy[0])):

300.

301.
if mapObjCopy[x][y] == '#':

302.
if (isWall(mapObjCopy, x, y - 1) and isWall(mapObjCopy, x + 1, y)) or \
 \
        303.(isWall(mapObjCopy, x + 1, y) and isWall(mapObjCopy, x, y + 1)) or \
 \
        304.(isWall(mapObjCopy, x, y + 1) and isWall(mapObjCopy, x - 1, y)) or \
 \
        305.(isWall(mapObjCopy, x - 1, y) and isWall(mapObjCopy, x, y - 1)):

306.
mapObjCopy[x][y] = 'x'

307.

308. elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < OUTSIDE_DECORATION_PCT:

309.
mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))

310.

311.
return mapObjCopy

312.

313.

314.


def isBlocked(mapObj, gameStateObj, x, y):


315.
"""Returns True if the (x, y) position on the map is

316.     blocked by a wall or star, otherwise return False."""

317.

318.
if isWall(mapObj, x, y):

319.
return True

320.

321. elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):

322.
return True  # x and y aren't actually on the map.

323.

324. elif (x, y) in gameStateObj['stars']:

325.
return True  # a star is blocking

326.

327.
return False

328.

329.

330.


def makeMove(mapObj, gameStateObj, playerMoveTo):


331.
"""Given a map and game state object, see if it is possible for the

332.     player to make the given move. If it is, then change the player's

333.     position (and the position of any pushed star). If not, do nothing.

334.

335.     Returns True if the player moved, otherwise False."""

336.

337.  # Make sure the player can move in the direction they want.

338.
playerx, playery = gameStateObj['player']

339.

340.  # This variable is "syntactic sugar". Typing "stars" is more

341.  # readable than typing "gameStateObj['stars']" in our code.

342.
stars = gameStateObj['stars']

343.

344.  # The code for handling each of the directions is so similar aside

345.  # from adding or subtracting 1 to the x/y coordinates. We can

346.  # simplify it by using the xOffset and yOffset variables.

347.
if playerMoveTo == UP:

348.
xOffset = 0

349.
yOffset = -1

350. elif playerMoveTo == RIGHT:

351.
xOffset = 1

352.
yOffset = 0

353. elif playerMoveTo == DOWN:

354.
xOffset = 0

355.
yOffset = 1

356. elif playerMoveTo == LEFT:

357.
xOffset = -1

358.
yOffset = 0

359.

360.  # See if the player can move in that direction.

361.
if isWall(mapObj, playerx + xOffset, playery + yOffset):

362.
return False

363. else:

364.
if (playerx + xOffset, playery + yOffset) in stars:

365.  # There is a star in the way, see if the player can push it.

366.
if not isBlocked(mapObj, gameStateObj, playerx + (xOffset * 2), playery + (yOffset * 2)):

367.  # Move the star.

368.
ind = stars.index((playerx + xOffset, playery + yOffset))

369.
stars[ind] = (stars[ind][0] + xOffset, stars[ind][1] + yOffset)

370. else:

371.
return False

372.  # Move the player upwards.

373.
gameStateObj['player'] = (playerx + xOffset, playery + yOffset)

374.
return True

375.

376.

377.


def startScreen():


378.
"""Display the start screen (which has the title and instructions)

379.     until the player presses a key. Returns None."""

380.

381.  # Position the title image.

382.
titleRect = IMAGESDICT['title'].get_rect()

383.
topCoord = 50  # topCoord tracks where to position the top of the text

384.
titleRect.top = topCoord

385.
titleRect.centerx = HALF_WINWIDTH

386.
topCoord += titleRect.height

387.

388.  # Unfortunately, Pygame's font & text system only shows one line at

389.  # a time, so we can't use strings with \n newline characters in them.

390.  # So we will use a list with each line in it.

391.
instructionText = ['Push the stars over the marks.',

                   392.                        'Arrow keys to move, WASD for camera control, P to change character.',

                   393.                        'Backspace to reset level, Esc to quit.',

                   394.                        'N for next level, B to go back a level.']

395.

396.  # Start with drawing a blank color to the entire window:

397.
DISPLAYSURF.fill(BGCOLOR)

398.

399.  # Draw the title image to the window:

400.
DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)

401.

402.  # Position and draw the text.

403.
for i in range(len(instructionText)):

404.
instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)

405.
instRect = instSurf.get_rect()

406.
topCoord += 10  # 10 pixels will go in between each line of text.

407.
instRect.top = topCoord

408.
instRect.centerx = HALF_WINWIDTH

409.
topCoord += instRect.height  # Adjust for the height of the line.

410.
DISPLAYSURF.blit(instSurf, instRect)

411.

412.
while True:  # Main loop for the start screen.

413.
for event in pygame.event.get():

414.
if event.type == QUIT:

415.
terminate()

416. elif event.type == KEYDOWN:

417.
if event.key == K_ESCAPE:

418.
terminate()

419.
return  # user has pressed a key, so return.

420.

421.  # Display the DISPLAYSURF contents to the actual screen.

422.
pygame.display.update()

423.
FPSCLOCK.tick()

424.

425.

426.


def readLevelsFile(filename):


427.
assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)

428.
mapFile = open(filename, 'r')

429.  # Each level must end with a blank line

430.
content = mapFile.readlines() + ['\r\n']

431.
mapFile.close()

432.

433.
levels = []  # Will contain a list of level objects.

434.
levelNum = 0

435.
mapTextLines = []  # contains the lines for a single level's map.

436.
mapObj = []  # the map object made from the data in mapTextLines

437.
for lineNum in range(len(content)):

438.  # Process each line that was in the level file.

439.
line = content[lineNum].rstrip('\r\n')

440.

441.
if ';' in line:

442.  # Ignore the ; lines, they're comments in the level file.

443.
line = line[:line.find(';')]

444.

445.
if line != '':

446.  # This line is part of the map.

447.
mapTextLines.append(line)

448. elif line == '' and len(mapTextLines) > 0:

449.  # A blank line indicates the end of a level's map in the file.

450.  # Convert the text in mapTextLines into a level object.

451.

452.  # Find the longest row in the map.

453.
maxWidth = -1

454.
for i in range(len(mapTextLines)):

455.
if len(mapTextLines[i]) > maxWidth:

456.
maxWidth = len(mapTextLines[i])

457.  # Add spaces to the ends of the shorter rows. This

458.  # ensures the map will be rectangular.

459.
for i in range(len(mapTextLines)):

460.
mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

461.

462.  # Convert mapTextLines to a map object.

463.
for x in range(len(mapTextLines[0])):

464.
mapObj.append([])

465.
for y in range(len(mapTextLines)):

466.
for x in range(maxWidth):

467.
mapObj[x].append(mapTextLines[y][x])

468.

469.  # Loop through the spaces in the map and find the @, ., and $

470.  # characters for the starting game state.

471.
startx = None  # The x and y for the player's starting position

472.
starty = None

473.
goals = []  # list of (x, y) tuples for each goal.

474.
stars = []  # list of (x, y) for each star's starting position.

475.
for x in range(maxWidth):

476.
for y in range(len(mapObj[x])):

477.
if mapObj[x][y] in ('@', '+'):

478.  # '@' is player, '+' is player & goal

479.
startx = x

480.
starty = y

481.
if mapObj[x][y] in ('.', '+', '*'):

482.  # '.' is goal, '*' is star & goal

483.
goals.append((x, y))

484.
if mapObj[x][y] in ('$', '*'):

485.  # '$' is star

486.
stars.append((x, y))

487.

488.  # Basic level design sanity checks:

489.
assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (
levelNum + 1, lineNum, filename)

490.
assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (
levelNum + 1, lineNum, filename)

491.
assert len(stars) >= len(
    goals), 'Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars.' % (
levelNum + 1, lineNum, filename, len(goals), len(stars))

492.

493.  # Create level object and starting game state object.

494.
gameStateObj = {'player': (startx, starty),

                495.                             'stepCounter': 0,

                                                                496.
'stars': stars}

497.
levelObj = {'width': maxWidth,

            498.                         'height': len(mapObj),

                                                   499.
'mapObj': mapObj,

500.
'goals': goals,

501.
'startState': gameStateObj}

502.

503.
levels.append(levelObj)

504.

505.  # Reset the variables for reading the next map.

506.
mapTextLines = []

507.
mapObj = []

508.
gameStateObj = {}

509.
levelNum += 1

510.
return levels

511.

512.

513.


def floodFill(mapObj, x, y, oldCharacter, newCharacter):


514.
"""Changes any values matching oldCharacter on the map object to

515.     newCharacter at the (x, y) position, and does the same for the

516.     positions to the left, right, down, and up of (x, y), recursively."""

517.

518.  # In this game, the flood fill algorithm creates the inside/outside

519.  # floor distinction. This is a "recursive" function.

520.  # For more info on the Flood Fill algorithm, see:

521.  # http://en.wikipedia.org/wiki/Flood_fill

522.
if mapObj[x][y] == oldCharacter:

523.
mapObj[x][y] = newCharacter

524.

525.
if x < len(mapObj) - 1 and mapObj[x + 1][y] == oldCharacter:

526.
floodFill(mapObj, x + 1, y, oldCharacter, newCharacter)  # call right

527.
if x > 0 and mapObj[x - 1][y] == oldCharacter:

528.
floodFill(mapObj, x - 1, y, oldCharacter, newCharacter)  # call left

529.
if y < len(mapObj[x]) - 1 and mapObj[x][y + 1] == oldCharacter:

530.
floodFill(mapObj, x, y + 1, oldCharacter, newCharacter)  # call down

531.
if y > 0 and mapObj[x][y - 1] == oldCharacter:

532.
floodFill(mapObj, x, y - 1, oldCharacter, newCharacter)  # call up

533.

534.

535.


def drawMap(mapObj, gameStateObj, goals):


536.
"""Draws the map to a Surface object, including the player and

537.     stars. This function does not call pygame.display.update(), nor

538.     does it draw the "Level" and "Steps" text in the corner."""

539.

540.  # mapSurf will be the single Surface object that the tiles are drawn

541.  # on, so that it is easy to position the entire map on the DISPLAYSURF

542.  # Surface object. First, the width and height must be calculated.

543.
mapSurfWidth = len(mapObj) * TILEWIDTH

544.
mapSurfHeight = (len(mapObj[0]) - 1) * (TILEHEIGHT - TILEFLOORHEIGHT) + TILEHEIGHT

545.
mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))

546.
mapSurf.fill(BGCOLOR)  # start with a blank color on the surface.

547.

548.  # Draw the tile sprites onto this surface.

549.
for x in range(len(mapObj)):

550.
for y in range(len(mapObj[x])):

551.
spaceRect = pygame.Rect((x * TILEWIDTH, y * (TILEHEIGHT - TILEFLOORHEIGHT), TILEWIDTH, TILEHEIGHT))

552.
if mapObj[x][y] in TILEMAPPING:

553.
baseTile = TILEMAPPING[mapObj[x][y]]

554. elif mapObj[x][y] in OUTSIDEDECOMAPPING:

555.
baseTile = TILEMAPPING[' ']

556.

557.  # First draw the base ground/wall tile.

558.
mapSurf.blit(baseTile, spaceRect)

559.

560.
if mapObj[x][y] in OUTSIDEDECOMAPPING:

561.  # Draw any tree/rock decorations that are on this tile.

562.
mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)

563. elif (x, y) in gameStateObj['stars']:

564.
if (x, y) in goals:

565.  # A goal AND star are on this space, draw goal first.

566.
mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)

567.  # Then draw the star sprite.

568.
mapSurf.blit(IMAGESDICT['star'], spaceRect)

569. elif (x, y) in goals:

570.  # Draw a goal without a star on it.

571.
mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)

572.

573.  # Last draw the player on the board.

574.
if (x, y) == gameStateObj['player']:

575.  # Note: The value "currentImage" refers

576.  # to a key in "PLAYERIMAGES" which has the

577.  # specific player image we want to show.

578.
mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

579.

580.
return mapSurf

581.

582.

583.


def isLevelFinished(levelObj, gameStateObj):


584.
"""Returns True if all the goals have stars in them."""

585.
for goal in levelObj['goals']:

586.
if goal not in gameStateObj['stars']:

587.  # Found a space with a goal but no star on it.

588.
return False

589.
return True

590.

591.

592.


def terminate():


593.
pygame.quit()

594.
sys.exit()

595.

596.

597.
if __name__ == '__main__':

598.
main()

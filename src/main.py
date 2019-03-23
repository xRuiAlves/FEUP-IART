from gameState import stateFromString

gameState = stateFromString('BBBJCCHooJoKHAAJoKooIDDLEEIooLooooGG')
print(gameState)

for gs in gameState.getAllStates():
    print(gs)

def buildBoard():
    size = int(input("Please select the size board that you would like to play on.\nEX: (3) 3x3 (4) 4x4 (5) 5x5 :"))
    board = []
    
    for i in range(size*size):
        board.append (i+1)
            
    if size == 3:
        print("")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("")
    
    elif size == 4:
        print("")
        print(f"  {board[0]} |  {board[1]} |  {board[2]} |  {board[3]} ")
        print("----+----+----+----")
        print(f"  {board[4]} |  {board[5]} |  {board[6]} |  {board[7]} ")
        print("----+----+----+----")
        print(f"  {board[8]} | {board[9]} | {board[10]} | {board[11]} ")
        print("----+----+----+----")
        print(f" {board[12]} | {board[13]} | {board[14]} | {board[15]} ")
        print("")
    elif size == 5:
        print("")
        print(f"  {board[0]} |  {board[1]} |  {board[2]} |  {board[3]} |  {board[4]} ")
        print("----+----+----+----+----")
        print(f"  {board[5]} |  {board[6]} |  {board[7]} |  {board[8]} | {board[9]} ")
        print("----+----+----+----+----")
        print(f" {board[10]} | {board[11]} | {board[12]} | {board[13]} | {board[14]} ")
        print("----+----+----+----+----")
        print(f" {board[15]} | {board[16]} | {board[17]} | {board[18]} | {board[19]} ")
        print("----+----+----+----+----")
        print(f" {board[20]} | {board[21]} | {board[22]} | {board[23]} | {board[24]} ")
    else:
        print("Invalid selection")

buildBoard()
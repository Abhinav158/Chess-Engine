import stockfish

sf = stockfish.Stockfish(r'"C:\Users\raghu\Downloads\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern.exe"')
sf.set_depth(20)
sf.set_skill_level(20)
sf.set_elo_rating(1600)
# print(sf.get_parameters())
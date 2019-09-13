# Copyright (c) 2019 Eric Steinberger


"""
This file is not runable; it's is a template to show how you could play against your algorithms. To do so,
replace "YourAlgorithmsEvalAgentCls" with the EvalAgent subclass (not instance) of your algorithm.

Note that you can see the AI's cards on the screen since this is just a research application and not meant for actual
competition. The AI can, of course, NOT see your cards.
"""

from PokerRL.game.InteractiveGameCustom import InteractiveGameCustom
from NFSP.EvalAgentNFSP import EvalAgentNFSP
from PokerRL.game.games import DiscretizedNLHoldem
from PokerRL.game import bet_sets

if __name__ == '__main__':
    eval_agent = EvalAgentNFSP.load_from_disk(
        path_to_eval_agent="eval_agent.pkl")

    round = 0

    playerAWinnings = 0
    playerBWinnings = 0

    while True:
        playerA = 500
        playerB = 500
        while playerA > 0 and playerB > 0:

            if round % 2 == 0:
                game_cls = DiscretizedNLHoldem
                args = game_cls.ARGS_CLS(n_seats=2,
                                         bet_sizes_list_as_frac_of_pot=bet_sets.B_5,
                                         starting_stack_sizes_list=(playerA, playerB)
                                         )

                game = InteractiveGameCustom(env_cls=game_cls,
                                       env_args=args,
                                       seats_human_plays_list=[0],
                                       eval_agent=eval_agent,
                                       )

                game.start_to_play()

                winnings = game.winnings_per_seat
                playerA += int(winnings[0])
                playerB += int(winnings[1])
            else:
                game_cls = DiscretizedNLHoldem
                args = game_cls.ARGS_CLS(n_seats=2,
                                         bet_sizes_list_as_frac_of_pot=bet_sets.B_5,
                                         starting_stack_sizes_list=(playerB, playerA)
                                         )

                game = InteractiveGameCustom(env_cls=game_cls,
                                             env_args=args,
                                             seats_human_plays_list=[1],
                                             eval_agent=eval_agent,
                                             )

                game.start_to_play()

                winnings = game.winnings_per_seat
                print(winnings)
                playerA += int(winnings[1])
                playerB += int(winnings[0])
        round+=1
        if playerA > 0:
            playerAWinnings+=1
        else:
            playerBWinnings+=1

        print('Winnings A:{} winnings B:{}'.format(playerAWinnings,playerBWinnings))

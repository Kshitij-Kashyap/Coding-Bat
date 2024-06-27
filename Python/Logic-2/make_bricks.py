def make_bricks(small, big, goal):
  max_big_bricks = min(big, goal // 5)
  remaining_goal = goal - (max_big_bricks * 5)
  return remaining_goal <= small

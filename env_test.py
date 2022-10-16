import time
import gym

print("游戏ID:\t\t\t\t\t\t\t\t 游戏名:\t\t\t\t\t\t\t\t  游戏类型:")
for env in gym.envs.registry.all():
    print('{:<35}  {:<35}  {:<15}'.format(env.id, env._env_name, env.entry_point.split(':')[1]))

print("\n\n游戏环境detail：")
print(env)
# print(type(gym.envs.registry.keys()))
# print(type(gym.envs.registry.values()))

print("\n\n环境测试阶段：")
a_time = time.time()
num = 0
for env in gym.envs.registry.all():
    try:
        env = gym.make(env.id, render_mode='human')
        obs = env.reset()
        for i in range(10):
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            # time.sleep(0.01)
        env.close()
    except Exception:
        num+=1
        print(env)
print("报错环境数为：", num)
print("用时：", time.time()-a_time)
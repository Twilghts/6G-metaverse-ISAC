import numpy as np
import tensorflow as tf
from tensorflow.keras import layers


# 定义智能体的策略网络和值函数网络
class ActorCritic(tf.keras.Model):
    def __init__(self, num_actions):
        super(ActorCritic, self).__init__()
        self.actor = self.build_actor(num_actions)
        self.critic = self.build_critic()

    def build_actor(self, num_actions):
        actor = tf.keras.Sequential([
            layers.Dense(256, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(num_actions, activation='tanh')
        ])
        return actor

    def build_critic(self):
        critic = tf.keras.Sequential([
            layers.Dense(256, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(1)
        ])
        return critic


# 定义DDPG智能体
class DDPGAgent:
    def __init__(self, num_actions):
        self.actor_critic = ActorCritic(num_actions)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

    def get_action(self, state):
        state = tf.convert_to_tensor([state], dtype=tf.float32)
        action = self.actor_critic.actor(state)
        return action[0]

    def train(self, states, actions, rewards, next_states, done):
        states = tf.convert_to_tensor(states, dtype=tf.float32)
        actions = tf.convert_to_tensor(actions, dtype=tf.float32)
        rewards = tf.convert_to_tensor(rewards, dtype=tf.float32)
        next_states = tf.convert_to_tensor(next_states, dtype=tf.float32)

        with tf.GradientTape() as tape:
            next_actions = self.actor_critic.actor(next_states, training=True)
            q_values = self.actor_critic.critic(next_states, training=True)
            target_q_values = rewards + (1 - done) * q_values
            critic_loss = tf.reduce_mean(tf.square(target_q_values - q_values))

        critic_grads = tape.gradient(critic_loss, self.actor_critic.critic.trainable_variables)
        self.critic_optimizer.apply_gradients(zip(critic_grads, self.actor_critic.critic.trainable_variables))

        with tf.GradientTape() as tape:
            actions = self.actor_critic.actor(states, training=True)
            q_values = self.actor_critic.critic(states, training=True)
            actor_loss = -tf.reduce_mean(q_values)

        actor_grads = tape.gradient(actor_loss, self.actor_critic.actor.trainable_variables)
        self.actor_optimizer.apply_gradients(zip(actor_grads, self.actor_critic.actor.trainable_variables))


# 创建多智能体环境并训练
num_agents = 2
num_actions = 2
num_episodes = 1000

agents = []
for _ in range(num_agents):
    agent = DDPGAgent(num_actions)
    agents.append(agent)

for episode in range(num_episodes):
    states = env.reset()
    total_reward = 0

    while not done:
        actions = [agent.get_action(state) for agent, state in zip(agents, states)]
        next_states, rewards, done, _ = env.step(actions)

        for agent in agents:
            agent.train(states, actions, rewards, next_states, done)

        states = next_states
        total_reward += np.sum(rewards)

    print(f"Episode: {episode + 1}, Reward: {total_reward}")

# 在训练完成后，可以使用训练好的模型来测试智能体的性能
test_states = env.reset()
done = False

while not done:
    test_actions = [agent.get_action(state) for agent, state in zip(agents, test_states)]
    test_next_states, _, done, _ = env.step(test_actions)
    test_states = test_next_states
    env.render()

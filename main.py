import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

os.makedirs("assets", exist_ok=True)

arr = [2, 7, 11, 15]
target = 17

num_dict = {}

fig, ax = plt.subplots(figsize=(10, 4))

def update(frame):
    ax.clear()
    ax.set_xlim(-1, len(arr))
    ax.set_ylim(0, 3)
    ax.set_xticks(range(len(arr)))
    ax.set_yticks([])
    ax.set_title("Two Sum - Hashmap Approach")

    # Display the input array and target value
    input_text = f"Array: {arr}, Target: {target}"
    ax.text(0, 2.5, input_text, fontsize=14, ha='left', color="blue")

    # Plot array elements
    for i, num in enumerate(arr):
        color = "blue" if i != frame else "orange"
        ax.scatter(i, 1, color=color, s=100)
        ax.text(i, 1.1, str(num), ha='center', fontsize=12)

    # Iterate over the array
    if frame < len(arr):
        num = arr[frame]
        complement = target - num

        # Display the complement value
        ax.text(frame, 1.3, f"Complement: {complement}", fontsize=12, ha='center', color="black")

        # Check if complement exists in the dictionary
        if complement in num_dict:
            comp_index = num_dict[complement]
            ax.scatter(comp_index, 1, color="red", s=200, label="Complement")
            ax.scatter(frame, 1, color="green", s=200, label="Current")
            ax.text(frame, 1.5, "Found!", color="purple", fontsize=12, ha='center')
        else:
            num_dict[num] = frame

    # Display the current state of the dictionary
    dict_text = "Dict: " + ", ".join([f"{k}: {v}" for k, v in num_dict.items()])
    ax.text(0, 2.8, dict_text, fontsize=12, ha='left')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(arr), interval=2000, repeat=False)

# Save animation as GIF
gif_path = "assets/two_sum_animation.gif"
ani.save(gif_path, writer="pillow", fps=1)

print(f"GIF saved at: {gif_path}")

plt.show()
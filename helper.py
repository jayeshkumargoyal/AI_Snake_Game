import matplotlib.pyplot as plt
from IPython import display

# Enable interactive mode for real-time plot updates
plt.ion()

def plot(scores, mean_scores):
    """
    Visualizes training progress with dynamic updates in Jupyter notebooks.
    
    Args:
        scores: List of raw scores from each game
        mean_scores: List of rolling average scores
    
    Features:
        - Dual line plot (raw scores + moving average)
        - Auto-scaling y-axis starting from 0
        - Latest value annotations
        - Non-blocking updates
    """

    # Clear previous output and get current figure context
    display.clear_output(wait=True)
    display.display(plt.gcf())

    # Reset the figure for fresh drawing
    plt.clf()

    # Configure plot aesthetics
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')

    # Plot both raw and averaged scores
    plt.plot(scores)
    plt.plot(mean_scores)

    # Set axis limits and add legend
    plt.ylim(ymin=0)

    # Annotate latest values
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))

    # Display plot without blocking execution
    plt.show(block=False)

    # Brief pause to allow graphics rendering
    plt.pause(.1)
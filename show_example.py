# Import dependencies
from explore_kitti_lib import *

# Choose input data
date = '2011_09_26'
drive = '0001'

# Load dataset
dataset = load_dataset(date, drive)

# Load tracklets (rects and types)
tracklet_rects, tracklet_types = load_tracklets_for_frames(len(list(dataset.velo)), 'data/{}/{}_drive_{}_sync/tracklet_labels.xml'.format(date, date, drive))

# Display fram statistics
frame = 10
display_frame_statistics(dataset, tracklet_rects, tracklet_types, frame)

# Render frames animation
frames = []
n_frames = len(list(dataset.velo))
print('Preparing animation frames...')
for i in range(n_frames):
    print_progress(i, n_frames - 1)
    filename = draw_3d_plot(i, dataset, tracklet_rects, tracklet_types)
    frames += [filename]
print('...Animation frames ready.')
clip = ImageSequenceClip(frames, fps=5)

# Store animation
clip.write_gif('pcl_data.gif', fps=5)
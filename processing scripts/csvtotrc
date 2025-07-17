import pandas as pd
import os

def csv_to_trc(csv_filename):
    data_rate = 360
    orig_data_start_frame = 1
    
    df = pd.read_csv(csv_filename)
    
    marker_columns = [
        'rear_ankle_jc', 'rear_hip', 'elbow_jc', 'hand_jc',
        'rear_knee_jc', 'shoulder_jc', 'wrist_jc', 'lead_ankle_jc',
        'lead_hip', 'glove_elbow_jc', 'glove_hand_jc', 'lead_knee_jc',
        'glove_shoulder_jc', 'glove_wrist_jc', 'thorax_ap',
        'thorax_dist', 'thorax_prox', 'centerofmass'
    ]

    output_dir = os.path.join(os.path.dirname(csv_filename), 'newtrc')
    os.makedirs(output_dir, exist_ok=True)

    sessions = df['session_pitch'].unique()

    for session in sessions:
        session_df = df[df['session_pitch'] == session].reset_index(drop=True)
        num_frames = len(session_df)
        
        header = [
            'PathFileType\t4\t(X/Y/Z)\t{}.trc'.format(session),
            'DataRate\tCameraRate\tNumFrames\tNumMarkers\tUnits\tOrigDataRate\tOrigDataStartFrame\tOrigNumFrames',
            f'{data_rate}\t{data_rate}\t{num_frames}\t{len(marker_columns)}\tmm\t{data_rate}\t{orig_data_start_frame}\t{num_frames}'
        ]
        
        marker_names_row = ['Frame#', 'Time']
        for name in marker_columns:
            marker_names_row.extend([name, '', ''])
        
        coord_labels_row = ['', '']
        for i in range(1, len(marker_columns) + 1):
            coord_labels_row.extend([f'X{i}', f'Y{i}', f'Z{i}'])
        
        data_rows = []
        for idx, row in session_df.iterrows():
            frame_number = idx + 1
            time_value = row['time']
            data_row = [frame_number, time_value]
            for marker in marker_columns:
                x = row.get(f'{marker}_x', 0)
                y = row.get(f'{marker}_y', 0)
                z = row.get(f'{marker}_z', 0)
                data_row.extend([x, y, z])
            data_rows.append(data_row)
        
        trc_filename = os.path.join(output_dir, f'{session}.trc')
        with open(trc_filename, 'w') as f:
            for line in header:
                f.write(line + '\n')
            f.write('\t'.join(marker_names_row) + '\n')
            f.write('\t'.join(coord_labels_row) + '\n')
            f.write('\n')
            for data_row in data_rows:
                f.write('\t'.join(map(str, data_row)) + '\n')
        
        print(f'Created: {trc_filename}')
        break

if __name__ == "__main__":
    csv_filename = 'landmarks.csv'
    csv_to_trc(csv_filename)

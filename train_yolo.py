from ultralytics import YOLO
import csv
import time

def train_yolo():
    # Load a model
    model = YOLO('yolov8n.yaml')
    # Select a dataset
    dataset = 'CVC-ClinicDB.yaml'
    # Indicate the project name to save results
    project_name = 'CVC'

    # Hyperparameter configuration
    m_epochs = [100,200]
    m_batch = [16,32]
    m_opt = ["SGD","Adam"]
    m_lr = [0.001,0.0001]

    # Train the model for each configuration and save the results
    num_config=1
    for i in range(len(m_epochs)):
        for j in range(len(m_batch)):
            for k in range(len(m_opt)):
                for l in range(len(m_lr)):
                    # Take the initial time
                    start = time.time()

                    # Train the model using the selected dataset with the GPU (device=0)
                    # and save the results inside the project folder
                    model.train(data=dataset, epochs=m_epochs[i], batch=m_batch[j], optimizer=m_opt[k], lr0=m_lr[l], 
                                device=0, project=project_name, name="Config"+str(num_config))
                    # To train the model using pretrained weights include "pretrained=yolov8n.pt"

                    # Take the final time
                    end = time.time()
                    # Evaluate the model's performance on the validation set
                    results_val = model.val()
                    # Indicate file path for the specific configuration
                    file_path = project_name + "/" + "Config" + str(num_config)
                    # Save metrics results
                    with open(file_path+'metrics.csv','a') as f:
                        w = csv.writer(f)
                        w.writerow(results_val.results_dict.keys())
                        w.writerow(results_val.results_dict.values())
                    # Save speed results
                    with open(file_path+'speed.csv','a') as f:
                        w = csv.writer(f)
                        w.writerow(results_val.speed.keys())
                        w.writerow(results_val.speed.values())
                    # Save execution time results
                    t = end - start
                    d1 = {"t": t,}
                    with open(file_path+'exec_time.csv','a') as f:
                        w = csv.writer(f)
                        w.writerow(d1.keys())
                        w.writerow(d1.values())
                    # Increment the number to train the next configuration
                    num_config+=1

if __name__ == '__main__':
    train_yolo()
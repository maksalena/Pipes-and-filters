import cv2
import threading
import queue

class VideoCapturePipe:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source) # Capture from camera or file

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()

class Filter:
    def apply(self, frame):
        raise NotImplementedError("Subclasses must implement the apply method")

class BlackWhiteFilter(Filter):
    def apply(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to black and white

class MirrorFilter(Filter):
    def apply(self, frame):
        return cv2.flip(frame, 1) # Flip the frame horizontally (mirror effect)

class ResizeFilter(Filter):
    def apply(self, frame, scale=0.5):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        return cv2.resize(frame, (width, height))  # Resize the frame by scale

class EdgeDetectionFilter(Filter):
    def apply(self, frame):
        return cv2.Canny(frame, 100, 200) # Apply Canny edge detection

class PipeAndFilterProcessor:
    def __init__(self, filters):
        self.filters = filters
        self.pipes = [queue.Queue() for _ in range(len(filters) + 1)]  # Queues between filters

    def run_filter(self, filter_obj, input_queue, output_queue):
        while True:
            frame = input_queue.get()
            if frame is None:
                output_queue.put(None)  # Pass along the termination signal
                break
            processed_frame = filter_obj.apply(frame)
            output_queue.put(processed_frame)

    def start_pipeline(self):
        threads = []
        for i, filter_obj in enumerate(self.filters): # Start a thread for each filter
            thread = threading.Thread(target=self.run_filter, args=(filter_obj, self.pipes[i], self.pipes[i + 1]))
            thread.start()
            threads.append(thread)

        return threads

    def process_frame(self, frame):
        self.pipes[0].put(frame) # Put the frame into input queue

    def get_processed_frame(self):
        return self.pipes[-1].get() # Get the processed frame from output queue

    def stop_pipeline(self):
        self.pipes[0].put(None) # Signal stop

def main():
    video_pipe = VideoCapturePipe(0) # Initialize video capture from the webcam or file

    # Create filters
    filters = [
        BlackWhiteFilter(),
        MirrorFilter(),
        ResizeFilter(),
        EdgeDetectionFilter()
    ]

    
    processor = PipeAndFilterProcessor(filters) # Create the pipe-and-filter processor
    threads = processor.start_pipeline()

    while True:
        frame = video_pipe.read_frame()
        if frame is None:
            break 

        processor.process_frame(frame) # Send the frame to the pipeline
        processed_frame = processor.get_processed_frame() # Process the frame through the filters
        cv2.imshow('Processed Video', processed_frame)  # Show the processed frame

        if cv2.waitKey(1) & 0xFF == ord('q'): # Stop if 'q' pressed
            break

    processor.stop_pipeline()

    for thread in threads:
        thread.join()

    video_pipe.release() # Release video capture and close windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

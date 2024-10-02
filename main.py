import cv2

class VideoCapturePipe:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)  # Capture from camera

    def read_frame(self):
        ret, frame = self.cap.read() # Read one frame from the source
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release() # Release the video capture

class Filter:
    def apply(self, frame):
        raise NotImplementedError("Subclasses must implement this method")

class BlackWhiteFilter(Filter):
    def apply(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to black and white

class MirrorFilter(Filter):
    def apply(self, frame):
        return cv2.flip(frame, 1) # Flip the frame horizontally (mirror effect)

class ResizeFilter(Filter):
    def apply(self, frame, scale=0.5):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        return cv2.resize(frame, (width, height)) # Resize the frame by scale

class EdgeDetectionFilter(Filter):
    def apply(self, frame):
        return cv2.Canny(frame, 100, 200) # Apply Canny edge detection

class PipeAndFilterProcessor:
    def __init__(self, filters):
        self.filters = filters

    def process(self, frame):
        for filter in self.filters:  # Pass the frame through each filter
            frame = filter.apply(frame)
        return frame

def main():
    video_pipe = VideoCapturePipe(0)  # Initialize video capture from the webcam

    # Create filters
    filters = [
        BlackWhiteFilter(),
        MirrorFilter(),
        ResizeFilter(),
        EdgeDetectionFilter()
    ]

    processor = PipeAndFilterProcessor(filters)  # Create the pipe-and-filter processor

    while True:
        frame = video_pipe.read_frame()
        if frame is None:
            break

        processed_frame = processor.process(frame)  # Process the frame through the filters
        cv2.imshow('Processed Video', processed_frame) # Show the processed frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop if 'q' pressed
            break

    video_pipe.release() # Release video capture and close windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

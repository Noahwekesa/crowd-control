navigator.mediaDevices
  .getUserMedia({ video: true })
  .then((stream) => {
    const video = document.getElementById("live-camera");
    video.srcObject = stream;
  })
  .catch((error) => {
    console.error("Error accessing camera:", error);
  });

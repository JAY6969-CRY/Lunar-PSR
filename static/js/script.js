// script.js

// Basic setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('moon-container').appendChild(renderer.domElement);

// Create moon
const geometry = new THREE.SphereGeometry(5, 32, 32);
const texture = new THREE.TextureLoader().load('https://cdn.pixabay.com/photo/2015/05/15/14/51/moon-765165_960_720.jpg');
const material = new THREE.MeshBasicMaterial({ map: texture });
const moon = new THREE.Mesh(geometry, material);
scene.add(moon);

// Position camera
camera.position.z = 15;

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    moon.rotation.y += 0.01; // Rotate moon
    renderer.render(scene, camera);
}
animate();

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Alert on form submission
document.getElementById('upload-form').onsubmit = function() {
    alert('Image is being processed, please wait...');
};

<?php
session_start();

// Database connection
$servername = "localhost";
$username = "root";
$password = "Beechem@31426";
$dbname = "UserDetail";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
session_start();

// Check if the 'message' key exists in the session
if (isset($_SESSION['message'])) {
    echo $_SESSION['message'];
} else {
    echo "No message set.";
}
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Prepare and bind
    $stmt = $conn->prepare("SELECT userIdNo, password FROM users WHERE gmailId = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    // Check if user exists
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($userIdNo, $hashed_password);
        $stmt->fetch();

        // Verify password
        if (password_verify($password, $hashed_password)) {
            $_SESSION['userIdNo'] = $userIdNo;
            echo "Signed in successfully!";
            // Redirect to a protected page
            header("Location: signin.php");
            exit();
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "No user found with that email.";
    }

    $stmt->close();
}

$conn->close();
?>

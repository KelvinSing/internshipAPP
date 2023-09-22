<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>JobEntry - Job Portal Website Template</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="" name="keywords">
    <meta content="" name="description">

    <!-- Favicon -->
    <link href="/assets/img/favicon.icon" rel="icon">

    <!-- Google Web Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600&family=Inter:wght@700;800&display=swap"
        rel="stylesheet">

    <!-- Icon Font Stylesheet -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">

    <!-- Libraries Stylesheet -->
    <link href="/assets/lib/animate/animate.min.css" rel="stylesheet">
    <link href="/assets/lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">

    <!-- Customized Bootstrap Stylesheet -->
    <link href="/assets/css/bootstrap.min.css" rel="stylesheet">

    <!-- Template Stylesheet -->
    <link href="/assets/css/style.css" rel="stylesheet">

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--link rel="stylesheet" href="css/style2.css"-->
    <!--jQuery CDN Link-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <style>
        body,
        html {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 50px;
            /* Adjust margin as needed */
        }

        .btn-container button {
            margin: 10px;
        }

        .logInPage {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .form {
            width: 600px;
            padding: 50px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .signUpBtn,
        .loginBtn {
            padding: 10px;
            margin: 10px;
            border: none;
            border-radius: 8px;
            cursor: pointer;

        }


        .loginBtn {
            margin-left: 10px;
            background-color: #008CBA;
            color: white;
            padding-left: 20px;
            padding-right: 20px;
        }


        .signUpBtn {
            background-color: #4CAF50;
            color: white;
        }


        .signUpForm,
        .loginForm {
            display: none;
        }

        .formGroup {
            margin-bottom: 10px;
        }

        textarea#companyAddress,
        textarea#companyDescription,
        select#industry {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #cccccc;
            box-sizing: border-box;
            color: #393a3a;
            font-size: 16px;
            /* Adjust the font size as needed */
            margin-bottom: 10px;
            /* Added margin for spacing */
        }

        label {
            display: block;
            margin-bottom: 5px;
        }

        input {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #cccccc;
            box-sizing: border-box;
            color: #393a3a;
        }


        .formGroup label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            margin-top: 20px;
            /* Optional: Make the label bold */
        }

        .checkBox {
            padding: 0px -200px;
        }

        .checkBox input {
            margin-right: 10px;
        }

        .checkbox .text {
            flex-grow: 1;
            display: inline;
        }


        .btn2 {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #008CBA;
            color: white;
        }

        .btn2:hover {
            background-color: #005f6b;
        }
    </style>
</head>

<body>
    <div class="container-xxl bg-white p-0">
        <!-- Spinner Start -->
        <div id="spinner"
            class="show bg-white position-fixed translate-middle w-100 vh-100 top-50 start-50 d-flex align-items-center justify-content-center">
            <div class="spinner-border text-primary" style="width: 3rem; height: 3rem;" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <!-- Spinner End -->


        <!-- Navbar Start -->
        <nav class="navbar navbar-expand-lg bg-white navbar-light shadow sticky-top p-0">
            <a href="/" class="navbar-brand d-flex align-items-center text-center py-0 px-4 px-lg-5">
                <h1 class="m-0 text-primary">JobEntry</h1>
            </a>
            <button type="button" class="navbar-toggler me-4" data-bs-toggle="collapse"
                data-bs-target="#navbarCollapse">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <div class="navbar-nav ms-auto p-4 p-lg-0">
                    <a href="/" class="nav-item nav-link">Home</a>
                    <a href="/about" class="nav-item nav-link">About</a>
                    <div class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Jobs</a>
                        <div class="dropdown-menu rounded-0 m-0">
                            <a href="/job-list" class="dropdown-item">Job List</a>
                            <a href="/job-detail" class="dropdown-item">Job Detail</a>
                        </div>
                    </div>
                    <div class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle active" data-bs-toggle="dropdown">Pages</a>
                        <div class="dropdown-menu rounded-0 m-0">
                            <a href="/category" class="dropdown-item">Job Category</a>
                            <a href="/testimonial" class="dropdown-item">Testimonial</a>
                            <a href="/404" class="dropdown-item active">404</a>
                        </div>
                    </div>
                    <a href="/contact" class="nav-item nav-link">Contact</a>
                </div>
                <div class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Login</a>
                    <div class="dropdown-menu rounded-0 m-0">
                        <a href="/student-login" class="dropdown-item">Login as Student</a>
                        <a href="/lecturer-login" class="dropdown-item">Login as Lecturer</a>
                        <a href="/company-login" class="dropdown-item">Login as Company</a>
                        <a href="/admin-login" class="dropdown-item">Login as Admin</a>
                    </div>
                </div>
                <a href="/post-job" class="btn btn-primary rounded-0 py-4 px-lg-5 d-none d-lg-block">Post A Job<i
                        class="fa fa-arrow-right ms-3"></i></a>
            </div>
        </nav>
        <!-- Navbar End -->


        <!-- Header End -->
        <div class="container-xxl py-5 bg-dark page-header mb-5">
            <div class="container my-5 pt-5 pb-4">
                <h1 class="display-3 text-white mb-3 animated slideInDown">Login</h1>
                <nav aria-label="breadcrumb">
                    <ol class="breadcrumb text-uppercase">
                        <li class="breadcrumb-item"><a href="#">Home</a></li>
                        <li class="breadcrumb-item"><a href="#">Pages</a></li>
                        <li class="breadcrumb-item text-white active" aria-current="page">Login</li>
                    </ol>
                </nav>
            </div>
        </div>
        <!--display center-->
        <div class="btn-container">
            <button class="signUpBtn" onclick="showSignUpForm()" style="margin: 10%;">SIGN UP</button>
            <button class="loginBtn" onclick="showLogInForm()">Login</button>
        </div>

        <div class="logInPage" style="display: none;">
            <div class="form" style="padding-top: 50px; margin-top: -100px;">
                <!--Sign Up Form-->
                <form class="signUp" id="signUpForm" style="display: none;" enctype="multipart/form-data"
                    action="/company-register" method="POST">
                    <div class="formGroup">
                        <label for="companyName">Company Name: </label>
                        <input type="text" id="companyName" name="Company_Name" required>
                    </div>
                    <div class="formGroup">
                        <label for="companyEmail">Company Email: </label>
                        <input type="email" placeholder="xxx@gmail.com" name="Company_Email" id="companyEmail" required>
                        <!--ori ID: signUpEmail-->
                    </div>
                    <div class="formGroup">
                        <label for="companyDescription">Company Description: </label>
                        <textarea id="companyDescription" name="Company_Description" rows="6" cols="59" required></textarea>
                    </div>
                    <div class="formGroup">
                        <label for="companyAddress">Company Address: </label>
                        <textarea id="companyAddress" name="Company_Address" rows="6" cols="59" required></textarea>
                    </div>
                    <div class="formGroup">
                        <label for="contactNumber">Contact Number: </label>
                        <input type="tel" id="contactNumber" name="Contact_Number" required>
                    </div>
                    <div class="formGroup">
                        <label for="websiteURL">Website URL: </label>
                        <input type="text" id="websiteURL" name="Website_URL" required>
                    </div>
                    <div class="formGroup">
                        <label for="industry">Industry: </label>
                        <select id="industry" name="Industry" class="textInput" required>
                            <option value="" disabled selected>Select an Industry</option>
                            <option value="Technology">Technology</option>
                            <option value="Finance">Finance</option>
                            <option value="Engineering">Engineering</option>
                            <option value="Marketing">Marketing</option>
                            <option value="Accounting">Accounting</option>
                        </select>
                    </div>
                    <div class="formGroup">
                        <label for="companySize">Company Size: </label>
                        <input type="text" id="companySize" name="Company_Size" required>
                    </div>
                    <div class="formGroup">
                        <label for="companyLogo">Company Logo:</label>
                        <input type="file" id="companyLogo" name="Company_Logo" accept="image/*" required>
                    </div>
                    <div class="formGroup">
                        <label for="compPassword">Password:</label>
                        <input type="password" id="compPassword" name = "Password" required autocomplete="off">
                    </div>
                    <div class="formGroup">
                        <label for="compPassword">Confirm Password :</label>
                        <input type="password" id="compPassword" required autocomplete="off">
                    </div>
                    <div class="checkBox" style="padding-bottom: 20px;">
                        <input type="checkbox" name="checkbox" id="checkbox" style="margin-left: -295px;">
                        <span class="text" style="margin-left: -280px;">I agree with term & conditions</span>
                    </div>
                    <div class="formGroup">
                        <button type="submit" class="btn2"><span>REGISTER</span></button>
                    </div>
                </form>

                <!--Login Form-->
                <form class="login" id="logInForm" style="display: none;" action="/get-company-details" method="POST">
                    <div class="formGroup">
                        <input type="email" placeholder="xxx@gmail.com" name="Company_Email" id="logInEmail" required
                            autocomplete="off" style="color: #393a3a;">
                    </div>
                    <div class="formGroup">
                        <input type="password" placeholder="Password" id="compPassword" name="Password" required
                            autocomplete="off" style="color: #393a3a;">
                    </div>
                    <div class="checkBox" style="margin-bottom: 15px;">
                        <input type="checkbox" name="checkbox" id="checkbox"
                            style="color: #393a3a; margin-left: -295px;">
                        <span class="text" style="margin-left: -280px;">Keep me signed in on this device</span>
                    </div>
                    <div class="formGroup">
                        <button type="submit" class="btn2" id="log">LOGIN</button>
                    </div>
                </form>
            </div>
        </div>
        <!-- Footer Start -->
        <div class="container-fluid bg-dark text-white-50 footer pt-5 mt-5 wow fadeIn" data-wow-delay="0.1s">
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-lg-3 col-md-6">
                        <h5 class="text-white mb-4">Company</h5>
                        <a class="btn btn-link text-white-50" href="">About Us</a>
                        <a class="btn btn-link text-white-50" href="">Contact Us</a>
                        <a class="btn btn-link text-white-50" href="">Our Services</a>
                        <a class="btn btn-link text-white-50" href="">Privacy Policy</a>
                        <a class="btn btn-link text-white-50" href="">Terms & Condition</a>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <h5 class="text-white mb-4">Quick Links</h5>
                        <a class="btn btn-link text-white-50" href="">About Us</a>
                        <a class="btn btn-link text-white-50" href="">Contact Us</a>
                        <a class="btn btn-link text-white-50" href="">Our Services</a>
                        <a class="btn btn-link text-white-50" href="">Privacy Policy</a>
                        <a class="btn btn-link text-white-50" href="">Terms & Condition</a>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <h5 class="text-white mb-4">Contact</h5>
                        <p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i>Rewa, Madhya Pradesh, IND</p>
                        <p class="mb-2"><i class="fa fa-phone-alt me-3"></i>+91991919191</p>
                        <p class="mb-2"><i class="fa fa-envelope me-3"></i>info@ajaykumar.com</p>
                        <div class="d-flex pt-2">
                            <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-twitter"></i></a>
                            <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-facebook-f"></i></a>
                            <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-youtube"></i></a>
                            <a class="btn btn-outline-light btn-social" href=""><i class="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6">
                        <h5 class="text-white mb-4">Newsletter</h5>
                        <p>Dolor amet sit justo amet elitr clita ipsum elitr est.</p>
                        <div class="position-relative mx-auto" style="max-width: 400px;">
                            <input class="form-control bg-transparent w-100 py-3 ps-4 pe-5" type="text"
                                placeholder="Your email">
                            <button type="button"
                                class="btn btn-primary py-2 position-absolute top-0 end-0 mt-2 me-2">SignUp</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="copyright">
                    <div class="row">
                        <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                            &copy; <a class="border-bottom" href="#">Your Site Name</a>, All Right Reserved.

                            <!--/*** This template is free as long as you keep the footer author’s credit link/attribution link/backlink. If you'd like to use the template without the footer author’s credit link/attribution link/backlink, you can purchase the Credit Removal License from "https://htmlcodex.com/credit-removal". Thank you for your support. ***/-->
                            Designed By <a class="border-bottom" href="">Code By Ajay Kumar</a>
                        </div>
                        <div class="col-md-6 text-center text-md-end">
                            <div class="footer-menu">
                                <a href="">Home</a>
                                <a href="">Cookies</a>
                                <a href="">Help</a>
                                <a href="">FQAs</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer End -->
        <script src="/assets/js/main.js"></script>
        <script>
            function showSignUpForm() {
                var signUpForm = document.getElementById('signUpForm');
                var logInForm = document.getElementById('logInForm');
                signUpForm.style.display = 'block';
                logInForm.style.display = 'none';
                showLogInPage();
            }

            function showLogInForm() {
                var signUpForm = document.getElementById('signUpForm');
                var logInForm = document.getElementById('logInForm');
                signUpForm.style.display = 'none';
                logInForm.style.display = 'block';
                showLogInPage();
            }

            function showLogInPage() {
                var logInPage = document.querySelector('.logInPage');
                logInPage.style.display = 'flex';
            }

            function registerUser() {
                // Add your registration logic here based on the selected role.
                var role = document.getElementById('role').value;
                // You can use the role value to customize the registration process.
                console.log('Registering user as ' + role);
            }
        </script>

        {% if error_message %}
        <script>
            alert('{{ error_message }}');
        </script>
        {% endif %}
        
        {% if show_msg %}
        <script>
            alert('{{ show_msg }}');
        </script>
        {% endif %}
</body>

</html>

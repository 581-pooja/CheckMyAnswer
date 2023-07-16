# CheckMyAnswer
The evaluation of subjective answers has long been a challenge for educators, employers, and  researchers. CheckMyAnswer, powered by machine learning algorithms, 
has emerged as a  solution to this challenge.

Traditional methods of grading and assessment can be time-consuming, prone to human error. As 
a result, organizations may struggle to accurately assess the answers provided by employees or 
students, leading to suboptimal performance and decreased productivity. CheckMyAnswer 
provides a solution by automating the evaluation process and providing more accurate and 
efficient feedback.

# Dataset
Dataset Link: https://nlp.stanford.edu/projects/snli/

# Requirements:

- Python 3
- Colab
- Flask (Deployment)

## Design of System:
![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYVxwVPxXSbRBfrKvOlN8Wy5dpTzrMGqLIspUJMQBHX5jv-KlcYXTVO0AtJcqT72d5BTAXe1XPH2YY2VOK35V_V7GnhGyHRFqasQmdsDn0Vv8jZTzyrzekfqj-TRkCmv6dfs8XY1ojcX_WF3eeGZitXkBUMBpm8IDHURb-KFo0Orx7RG0j-D5RsLp-nW6F/s1600/Home4.png)

## Screenshots
- Home Page of CheckMyAnswer:
![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOPUIqKY1W1q-bZaw2O0FIXfZT6fFMZtYsS8ePZMV8icms7Hu5R6guqTgkKxwBm9tPfCTcUFovUnJtojurcn9LItMTRCizsx5Hxxk4c3ge8RpL-4YgMdgEs0ywCif4EDAyJlbLVBy2o7Fjz8C3h1uOPSLBMd6W1suu_wDZKzQMrs_pDCZBTtwMpop1I0ea/s1600/Home.png)


- When answer by student and teacher is similar:
![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiygWMvTwZqQwfwt75TStQkIulYLumbDRQKXT0UtLflmriwBCLC9GlakzNsyc9b3PUFyJh2a29Q4hHY-eDONInB94UOQxeWE96LckMj_qVnY1jPR8mwaemEoZr18tjKsaGiyGCYqAhOsr6TTDb7OUjMGZjlVAaS0tWG7kPTqhNq7Gz7x_4ZNgUhQeSlm8uw/s1600/Home1.png)


- When answer by student is correct but wordings are different than teacher’s answer:
![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5_zIctHKxW5TWOQf9byn70Wdjtx_VTBZiMqzkH2xTY2ivKQKBHX2ad_PUJW72d9KRlVP9FpA1Cq5w7mOlLIR-kpmg4Yjjj_RfsB4OA1W0rSzp6qpbAQtiFR-q-PI9Na5BvVcVrcqMnQQIFalLEbaCG7-piLOyunP8P-gq4B7NzG-IlwBxPfBZlVHZ2WxR/s1600/Home2.png)


- When answer by student is wrong and doesn’t match to teacher answer:
![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWib_CJZWbG7YAeRHa80Fp1saMfIegXOKF_jkViWKNru_xuCy2L_SgQ_U9CslS3kQ5wJSLpdlvkS04WfOO_dEeYc35T72xdUr9SVDpR-9SoLyUFIA64YnzpF6vuPYI4Uu2Y-hqS4wh-v_RLzrCIfPOvSNkK1R0-kx_8WNrMTHtIyeldAeWlmLgmp2wBJ3S/s1600/Home3.png)

## Installation

Install my-project with pip

```bash
  # Installing virtualenv
  pip install virtualenv
  virtualenv <venv>

  # In cmd.exe
  venv\Scripts\activate.bat

  # Install requirements.py i.e. requried files
  pip install -r requirements.txt
```

## Deployment

To Run Python Code or run Server

```bash
  python main.py
```


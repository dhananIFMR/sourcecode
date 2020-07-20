import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from utils.charts import make_question_pie, make_bar
from utils.summary_table import make_summary_table
from utils.playground import make_playground_header

footercontent = [

        html.Div(
            children=[    
         html.Div(
            children=[ 
          dbc.Row(            
            children=[
                dbc.Col(
                    children=[
                    html.P("2020 © LEAD at Krea University"), 
                       
                    ],
                     className="col-md-6 paddzero"
                ),
                dbc.Col(
                    children=[
                        html.A("Privacy Policy", href="/privacy", target="_blank"),
                    ],
                    className="col-md-6 paddzero text_rgt"
                ),
            ],
            className="",
        ),  
],
            className="container paddzero",
        ),            
       
        ],
        className="footer",
        ),
        
    ]
    

def make_jumbotron(link_text, link_href):
    jumbotron = dbc.Jumbotron(
        [
            html.Div(
                children=[
                    html.A(
                        [
                            html.Img(
                                src="/assets/lead-logo-new.png", className="ifmrlogo"
                            )
                        ],
                        href="https://ifmrlead.org/",
                        target="_blank",
                    ),
                    html.A(
                        [html.Img(src="/assets/game-logo.png", className="gamelogo")],
                        href="https://massentrepreneurship.org/",
                        target="_blank",
                    ),
                ],
                className="head-box container",
            ),
            html.Div(
                children=[
                    html.H2(
                        "Impact of COVID-19 on Microenterprises in India",
                        className="app-header",
                    ),
                    html.Div(
                        children=[
                            html.H3("Introduction", className="sub-head"),
                            html.Div(
                                children=[
                                    html.Span(
                                        """ A new collaborative study by """,
                                        className="linklead",
                                    ),
                                    html.A(
                                        "GAME",
                                        href="https://massentrepreneurship.org/",
                                        target="_blank",
                                    ),
                                    html.Span(""" and """, className="linklead"),
                                    html.A(
                                        "LEAD at Krea University",
                                        href="https://ifmrlead.org/",
                                        target="_blank",
                                    ),
                                    html.Span(
                                        """ at Krea University seeks to capture the status of micro-enterprises in India during the COVID-19 crisis. Through a multidimensional survey of microbusinesses being conducted over six months, the study will capture key trends on the impact of the COVID crisis and government-mandated lockdowns on business livelihoods, employment, and the income of nano and microbusinesses.  Additionally, the survey will also provide reliable estimates on business and employment outcomes and gauge confidence levels of small businesses in the economy periodically.""",
                                        className="linklead",
                                    ),
                                    html.Br(className=""),
                                    html.Div(
                                        """ This dashboard presents results from the ongoing survey and allows visitors to explore and visualise the data.""",
                                        className="linklead2",
                                    ),
                                ],
                                className="link-text",
                            ),
                        ],
                        className="desbox",
                    ),
                    html.Div(
                        children=[
                            html.H3("Collaborative study", className="sub-headrgt"),
                             html.Div(
                                children=[
                                    html.Span(
                                        """ This collaborative study has been conducted by partnering with organisations across a wide range of spectrum such as financial institutions, development sector organisations, fintech startups among others. Some of our key sample partners include """,
                                        className="linklead",
                                    ),
                                    html.A(
                                        " AYE Finance,",
                                        href="https://ayefin.com/",
                                        target="_blank",
                                    ),                                   
                                    html.A(
                                        " Pay1,",
                                        href="https://pay1.in/",
                                        target="_blank",
                                    ),
                                    html.A(
                                        " MannDeshi",
                                        href="https://manndeshifoundation.org/",
                                        target="_blank",
                                    ),
                                    html.Span(
                                        """  But we are looking to further expand the scope of our study and are thus inviting suggestions on including more partners in the survey. At the same time, we also look forward to receiving feedback as well as any additional inputs that you feel can make the survey better. Please click the below button to provide us feedback.""",
                                        className="linklead",
                                    ),
                                    
                                ],
                                className="link-textrgt",
                            ),
                           
                            html.Br(),
                            html.P( html.A("Download the Dataset", href="https://docs.google.com/forms/d/e/1FAIpQLSdESdaQfiCLyENGsTMKTMf-D-e2BGKuTJQb_5x-tzmliimYlg/viewform",   target="_blank"), className="lead leadrgt"),
                        ],
                        className="desbox",
                    ),
                ],
                className="head-text",
            ),
            html.Hr(className="my-2"),
            html.P(dcc.Link(link_text, href=link_href), className="lead"),
          
        ]
    )
    return jumbotron


def index(responses, summary_table):
    business_recovery_data_plot = make_question_pie(
        responses, "How confident are you about recovery in a post-lockdown scenario?"
    )
    cash_recovery_plot = make_question_pie(
        responses, "How much cash reserves do you currently have?"
    )
    employment_plot = make_question_pie(responses, "Were employees laid off?")
    household_plot = make_bar(
        responses, "What household challenges did you face during the lockdown?"
    )
    row_style = {}

    return [
        dbc.Row(make_jumbotron("Explore", "/playground")),
       html.Div(
                children=[
        dbc.Row(
           style=row_style,
            children=[dbc.Col(
            children=[
                       html.H3("Overview"),
                       make_summary_table(responses, summary_table),
                       html.Br(),
                       html.Br(),
                       ],
                       className="col-md-12"
                       )
                       ],
                className=""
        ),
        dbc.Row(
            style=row_style,
            children=[
                dbc.Col(
                    children=[
                        html.H3(dcc.Link("Business Recovery", href="business")),
                        html.P("""Despite most businesses remaining closed during lockdown, 81% of the respondents suggested that they are confident of business recovery in a post COVID-29 scenario.
""", className ="overview_txt"),
                        html.P(""" (Click on the title to dive deeper into the section)""", className="overview_italic"),
                        business_recovery_data_plot,
                    ],
                     className="col-xs-12 col-sm-12 col-lg-6"
                ),
                dbc.Col(
                    children=[
                        html.H3(
                            dcc.Link("Credit/Loans/Financial Status", href="credit")
                        ),
                        html.P("""57% reported not having any cash reserves to survive. Further, 40% tried to borrow money to cover expenses. Only 14% of the overall borrowing was from formal borrowing sources.""", className ="overview_txt"),
                         html.P(""" (Click on the title to dive deeper into the section)""", className="overview_italic"),
                        cash_recovery_plot,
                    ],
                    className="col-xs-12 col-sm-12 col-lg-6"
                )
            ],
            className="",
        ),
       
        # html.Hr(className="my-2"),
        dbc.Row(
            style=row_style,
            children=[
                dbc.Col(
                    children=[
                        html.H3(dcc.Link("Employment", href="employment")),
                        html.P("""Interestingly, most of the respondents during our Month 1 Survey suggested that they have not laid off employees. 79% of the respondents said they did not lay off, while 13% suggested that they are not laying off but are unable to pay salaries.
""", className ="overview_txt"),
                        html.P(""" (Click on the title to dive deeper into the section)""", className="overview_italic"),
                        employment_plot,
                    ],
                    className="col-xs-12 col-sm-12 col-lg-6"
                ),
                dbc.Col(
                    children=[
                        html.H3(dcc.Link("Household Challenges", href="household")),
                        html.P("""Across all respondents, Female business owners faced more household challenges than men. 70% female business owners suggested inter house conflicts as the biggest challenge while 53% men responded to the same. Women also faced more unaffordable expenses than men, with 46% suggesting the same.
""", className ="overview_txt"),
                     html.P(""" (Click on the title to dive deeper into the section)""", className="overview_italic"),
                        household_plot,
                    ],
                    className="col-xs-12 col-sm-12 col-lg-6"
                )
                
            ],
          
        ),
          
         
        ],
         className = "container overviewpage",
        ),
        
         html.Div(
                children=[
        html.Div(
                children=[
                 dbc.Row(
            style=row_style,
            children=[
                dbc.Col(
                    children=[                   
                        html.H3("Survey Methodology", className = "text-center"),
                        html.P("""Our stratified, convenience sample was drawn from various sub-industries in manufacturing, services and trade to provide a sectoral representation of microbusinesses. The sample was selected from lists provided by partner organizations. The following regions and states will be covered in the survey: North India (Delhi, Haryana, Punjab, Uttar Pradesh), South India (Tamil Nadu), West India (Gujarat, Maharashtra, Rajasthan). The surveys were conducted telephonically in the area’s local language, and each survey took 18-25 minutes to administer""",
                        className ="survey_txt"),
                            ],
                    className="paddzero"
                ),
               
               
            ],
             className=""
            
          
        ),
        ],
                  className = "container paddzero"
                ),
       
                ],
                  className = "overviewpage"
                ),
                
      
       
       
    ]+ footercontent


def business(responses):
    questions = [
        "What is the type of business you operate?",
        "How confident are you about recovery in a post-lockdown scenario?",
        "What was your business status during the lockdown?",
        "Does your business fall under Essential services?",
        """Is your business registered under any sort of 
Government registration?""",
        "How would you rate your business performance prior to the lockdown, based on your expectation?",
        "What are the challenges you faced in business operations?",
        "What coping strategies do you plan on adopting for business recovery?",
        "What is the expected timeline for business recovery for you?",
        "Do you plan to apply for any government relief packages?",
    ]
    plot_types = ["pie", "bar", "bar", "bar", "bar", "bar", "bar", "bar", "bar", "bar"]
    plot_list = []
    for question, plot_type in zip(questions, plot_types):
        if plot_type == "pie":
            plot_list.append(dbc.Row(dbc.Col(make_question_pie(responses, question))))
        if plot_type == "bar":
            plot_list.append(
                dbc.Row(dbc.Col(make_bar(responses, question)))
            )
    return [make_jumbotron("Back to Overview", "/")] + plot_list + footercontent


def employment(responses):
    questions = ["Were employees laid off?"]
    plot_types = ["bar"]
    plot_list = []
    for question, plot_type in zip(questions, plot_types):
        if plot_type == "pie":
            plot_list.append(dbc.Row(dbc.Col(make_question_pie(responses, question))))
        if plot_type == "bar":
            plot_list.append(
                dbc.Row(
                    dbc.Col(
                        make_bar(
                            responses, question, barmode="stack", orientation="h"
                        )
                    )
                )
            )
    return [make_jumbotron("Back to Overview", "/")] + plot_list + footercontent


def credit(responses):
    questions = [
        "How much cash reserves do you currently have?",
        "Did you dip into your savings ?",
        "Did you postpone any loan repayment due to cash crunch?",
        "Did you try borrowing to cover expenses?",
        "Were you able to secure a loan?",
        "Where did you get the loan from? (multiple choice)",
        "What is the status of payments to suppliers this month?",
        "What do you expect in terms of payments to suppliers next month?",
        "Are you getting paid by your customers?",
        "Why do you think there has been a change in the use of digital payments?",
        "How long have you been using these digital payments for your business?",
        "Overall, how do you think your usage of digital payments has changed during the lockdown?",
        "For what purposes has your usage of digital payments changed during the lockdown?",
        "Why do you think there has been a change in the use of digital payments?",
    ]
    plot_types = [
        "bar",
        "bar",
        "pie",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
        "bar",
    ]
    plot_list = []
    for question, plot_type in zip(questions, plot_types):
        if plot_type == "pie":
            plot_list.append(dbc.Row(dbc.Col(make_question_pie(responses, question))))
        if plot_type == "bar":
            plot_list.append(
                dbc.Row(dbc.Col(make_bar(responses, question)))
            )
    return [make_jumbotron("Back to Overview", "/")] + plot_list + footercontent


def household(responses):
    questions = [
        "Are you the sole earner for the household?",
        "What household challenges did you face during the lockdown?",
    ]
    plot_types = ["bar", "bar"]
    plot_list = []
    for question, plot_type in zip(questions, plot_types):
        if plot_type == "pie":
            plot_list.append(dbc.Row(dbc.Col(make_question_pie(responses, question))))
        if plot_type == "bar":
            plot_list.append(
                dbc.Row(dbc.Col(make_bar(responses, question)))
            )
    return [make_jumbotron("Back to Overview", "/")] + plot_list + footercontent


def playground(unique_states, unique_type_of_industry, unique_genders):
    playground = [
        dbc.Row(
            children=dbc.Col(
                make_playground_header(
                    unique_states, unique_type_of_industry, unique_genders
                )
            ),
            style={"padding-left": "50px", "padding-right": "50px"},
        )
    ]
    return [make_jumbotron("Back to Overview", "/")] + playground + footercontent
    
       
def privacy(responses):
    privacycontent = [
         html.Div(
            children=[    
         html.Div(
            children=[ 
          dbc.Row(            
            children=[
                dbc.Col(
                    children=[
                    html.Br(),
                    html.H3("Privacy Policy"),
                    html.P("At LEAD, we value and respect the privacy of our dashboard visitors, partners, customers and their end-users, and we believe that, in order for them to make informed choices about the use of their personal data, we must be transparent with respect to our privacy practices."), 
                    html.P("To ensure such transparency we have established the following Privacy Policy."), 
                    html.H5("INFORMATION WE COLLECT"),
                    html.P("When using or interacting with our dashboard, we may collect or receive the following types of information (collectively, “Information”)."),
                    html.Ol(
                    children=[
                    html.Li(children=[
                        html.Strong("Personal Information"),
                        html.Span(" such as name, email, contact details or any other personal content that you provide to us whether through a form or field on our app or any other communication (e.g. email, phone number)."),
                        ],
                        ),
                    html.Li(children=[
                        html.Strong("Technical Information"),
                        html.Span(" such as device type, operating system, IP address and other similar technical information typically received from the device automatically when visiting or interacting with our Platforms. This may include the referring URL that led you to our app."),
                        ],
                        ),
                    html.Li(children=[
                        html.Strong("Usage Information"),
                        html.Span(" such as the pages you visited on our app, where you clicked, searches performed on our app and other similar information related to how you have used our app. It may also include information related to whether you receive, opened or clicked on any links in an email sent to you."),
                        ],
                        ),
                    ],
                    className ="prilist",
                    ), 
                    html.Br(),
                    
                    ],
                     className="col-md-12 paddzero"
                ),
               
            ],
            className="",
        ),  
],
            className="container paddzero",
        ),            
       
        ],
        className="privacypage",
        ),
    ]
    
    return [make_jumbotron("Back to Overview", "/")] + privacycontent + footercontent

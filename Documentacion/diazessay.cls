%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Diaz Essay
% LaTeX Class
% Version 1.0 (13/1/19)
%
% This class originates from:
% http://www.LaTeXTemplates.com
%
% Authors:
% Vel (vel@LaTeXTemplates.com)
% Nicolas Diaz (nsdiaz@uc.cl)
%
% License:
% CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------------------------
%	CLASS CONFIGURATION
%----------------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{diazessay}[2019/01/13 Diaz Essay class v1.0]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}} % Pass through any options to the base class
\ProcessOptions\relax % Process given options

\LoadClass{article} % Load the base class

%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\usepackage[spanish]{babel} % English language hyphenation

\usepackage{graphicx} % Required for including images
\graphicspath{{Figures/}{./}} % Specifies where to look for included images (trailing slash required)

\usepackage{wrapfig} % Allows in-line images

\usepackage{booktabs} % Required for better horizontal rules in tables
\usepackage{url}


\usepackage{enumitem} % Required for list customisation
\setlist{noitemsep} % No spacing between list items

% CODE
% Default fixed font does not support bold face
\DeclareFixedFont{\ttb}{T1}{txtt}{bx}{n}{12} % for bold
\DeclareFixedFont{\ttm}{T1}{txtt}{m}{n}{12}  % for normal

% Custom colors
\usepackage{color}
\definecolor{deepblue}{rgb}{0,0,0.5}
\definecolor{deepred}{rgb}{0.6,0,0}
\definecolor{deepgreen}{rgb}{0,0.5,0}

\usepackage{listings}

% Python style for highlighting
\newcommand\pythonstyle{\lstset{
		language=Python,
		basicstyle=\ttm,
		otherkeywords={self},             % Add keywords here
		keywordstyle=\ttb\color{deepblue},
		emph={MyClass,__init__},          % Custom highlighting
		emphstyle=\ttb\color{deepred},    % Custom highlighting style
		stringstyle=\color{deepgreen},
		frame=tb,                         % Any extra options here
		showstringspaces=false            % 
}}


% Python environment
\lstnewenvironment{python}[1][]
{
	\pythonstyle
	\lstset{#1}
}
{}

% Python for external files
\newcommand\pythonexternal[2][]{{
		\pythonstyle
		\lstinputlisting[#1]{#2}}}

% Python for inline
\newcommand\pythoninline[1]{{\pythonstyle\lstinline!#1!}}

\makeatletter
\renewcommand\@biblabel[1]{\textbf{#1.}} % Remove the square brackets from each bibliography item ('[1]' to '1.')
\makeatother

%----------------------------------------------------------------------------------------
%	DOCUMENT MARGINS
%----------------------------------------------------------------------------------------

\usepackage{geometry} % Required for adjusting page dimensions and margins

\geometry{
	paper=a4paper, % Paper size, change to letterpaper for US letter size
	top=2.5cm, % Top margin
	bottom=3cm, % Bottom margin
	left=4cm, % Left margin
	right=4cm, % Right margin
	headheight=0.75cm, % Header height
	footskip=1.5cm, % Space from the bottom margin to the baseline of the footer
	headsep=0.75cm, % Space from the top margin to the baseline of the header
	%showframe, % Uncomment to show how the type block is set on the page
}

%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

\usepackage[utf8]{inputenc} % Required for inputting international characters
\usepackage[T1]{fontenc} % Use 8-bit encoding

\usepackage{mathpazo} % Use the Palatino font

\usepackage[protrusion=true, expansion=true]{microtype} % Better typography

\linespread{1.05} % Increase line spacing slightly; Palatino benefits from a slight increase by default

%----------------------------------------------------------------------------------------
%	TITLE
%----------------------------------------------------------------------------------------

\makeatletter
\renewcommand{\maketitle}{ % Customise the title (do not edit title and author name here)
	\vspace*{30pt} % Vertical whitespace before the title
	\begin{flushright} % Right align
		{\LARGE\@title} % Increase the font size of the title
		
		\vspace{50pt} % Vertical whitespace between the title and author name
		
		{\large\@author}\\Mario Pérez Sánchez-Montañez, David Camuñas Sánchez, Francesco Zingariello\\ 
		\@date % Date
		
		\vspace{40pt} % Vertical whitespace between the author block and abstract
	\end{flushright}
}
\makeatother

%----------------------------------------------------------------------------------------
%	HEADERS AND FOOTERS
%----------------------------------------------------------------------------------------

\usepackage{fancyhdr} % Required for customising headers and footers
\pagestyle{fancy} % Enable custom headers and footers

\renewcommand{\headrulewidth}{0pt} % Remove default top horizontal rule
\lhead{} % Left header
\chead{} % Centre header
\rhead{} % Right header
\lfoot{} % Left footer
\cfoot{\thepage} % Centre footer
\rfoot{} % Right footer

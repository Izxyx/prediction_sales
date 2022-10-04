mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#ffe400'\n\
backgroundColor = '#000000'\n\
secondaryBackgroundColor = '#ffe400'\n\
textColor = '#000000'\n\
" > ~/.streamlit/config.toml
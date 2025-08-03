from app import create_app

# Create Flask app instance using factory pattern
app = create_app()

if __name__ == '__main__':
    # Run the app on 0.0.0.0 to allow external access (useful for deployment)
    app.run(host='0.0.0.0', port=5000, debug=False)
def setup(app):
    extensions = [
        "breathe", "exhale",
    ]

    for ext in extensions:
        try:
            app.setup_extension(ext)
        except Exception as e:
            raise RuntimeError(
                f"Required extension {ext} is missing. Please install it."
            )

    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}

import streamlit as st

st.set_page_config(
    page_title="Bulk Text Cleaner & Transformer", page_icon="📝", layout="wide"
)

st.title("📝 Bulk Text Cleaner & Case Transformer")
st.write(
    "Paste your raw, messy text below and use the sidebar options to clean, format,"
    " and transform it instantly."
)

# Sidebar controls for transformation options
st.sidebar.header("🛠️ Cleaning Options")
case_option = st.sidebar.selectbox(
    "Change Case",
    [
        "None",
        "UPPERCASE",
        "lowercase",
        "Title Case",
        "Sentence case",
        "snake_case",
        "kebab-case",
    ],
)

st.sidebar.subheader("Formatting Adjustments")
remove_extra_spaces = st.sidebar.checkbox(
    "Remove Extra Spaces", value=True
)
remove_line_breaks = st.sidebar.checkbox(
    "Join Lines (Remove Line Breaks)", value=False
)
remove_duplicates = st.sidebar.checkbox("Remove Duplicate Lines", value=False)

# Main text area input
raw_text = st.text_area("Paste your text here:", height=200)

if raw_text:
  processed_text = raw_text

  # 1. Apply case transformations
  if case_option == "UPPERCASE":
    processed_text = processed_text.upper()
  elif case_option == "lowercase":
    processed_text = processed_text.lower()
  elif case_option == "Title Case":
    processed_text = processed_text.title()
  elif case_option == "Sentence case":
    # Simple sentence casing
    sentences = processed_text.split(". ")
    processed_text = ". ".join([s.capitalize() for s in sentences])
  elif case_option == "snake_case":
    processed_text = (
        processed_text.strip().lower().replace(" ", "_").replace("-", "_")
    )
  elif case_option == "kebab-case":
    processed_text = (
        processed_text.strip().lower().replace(" ", "-").replace("_", "-")
    )

  # 2. Apply formatting adjustments
  if remove_line_breaks:
    processed_text = " ".join(processed_text.splitlines())

  if remove_extra_spaces:
    # Collapse multiple spaces into one
    processed_text = " ".join(processed_text.split())

  if remove_duplicates:
    lines = processed_text.splitlines()
    seen = set()
    unique_lines = []
    for line in lines:
      if line not in seen:
        seen.add(line)
        unique_lines.append(line)
    processed_text = "\n".join(unique_lines)

  # Display real-time metrics
  st.markdown("---")
  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Characters", len(processed_text))
  col2.metric("Words", len(processed_text.split()))
  col3.metric("Lines", len(processed_text.splitlines()))
  col4.metric(
      "Est. Reading Time",
      f"{max(1, round(len(processed_text.split()) / 200, 1))} min",
  )

  # Output Result Section
  st.subheader("✨ Cleaned Output")
  st.text_area("Result:", value=processed_text, height=200)

  # Download button
  st.download_button(
      label="Download Cleaned Text as .txt",
      data=processed_text,
      file_name="cleaned_text.txt",
      mime="text/plain",
  )

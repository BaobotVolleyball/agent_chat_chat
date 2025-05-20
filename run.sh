function download_and_unzip() {
    local url=$1
    local dest_dir=$2

    if [ -d "$dest_dir" ]; then
        echo "Destination directory $dest_dir already exists. Skipping download."
        return
    fi

    mkdir -p "$dest_dir"

    local zip_file="${dest_dir}/downloaded.zip"
    echo "Downloading $url to $zip_file"
    curl -L -o "$zip_file" "$url"

    echo "Unzipping $zip_file to $dest_dir"
    unzip -o "$zip_file" -d "$dest_dir"

    rm "$zip_file"
    echo "Download and unzip completed successfully."
}
# Main script execution
pdf_js_version="4.0.379"
pdf_js_dist_name="pdfjs-${pdf_js_version}-dist"
pdf_js_dist_url="https://github.com/mozilla/pdf.js/releases/download/v${pdf_js_version}/${pdf_js_dist_name}.zip"
pdfjs_version_dist="libs/qcom/qcom/assets/prebuilt/${pdf_js_dist_name}" 
download_and_unzip "$pdf_js_dist_url" "$pdfjs_version_dist"

export MODULE_PATH=./MODEL_OCR
python app.py
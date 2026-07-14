#!/bin/bash

# 设置 UTF-8 编码支持（Linux 默认通常已支持）
export LANG=C.UTF-8

# 颜色定义 (ANSI Escape Codes)
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
RED='\033[0;31'
GREEN='\033[0;32m'
NC='\033[0m' # 重置颜色

export PATH="$PWD/venv/bin:$PATH"
export PATH="$PATH:/var/opt/orv_translate/jre17/bin"

# 统一步骤调用函数
invoke_step() {
    local step_number=$1
    local step_name=$2
    local script_path=$3

    echo -e "\n${CYAN}===============================================${NC}"
    echo -e "${YELLOW}         STEP ${step_number}: ${step_name}${NC}"
    echo -e "${CYAN}===============================================${NC}"

    # 运行虚拟环境中的 Python（Linux 路径为 ./venv/bin/python）
    ./venv/bin/python "$script_path"
    local last_exit_code=$?

    if [ $last_exit_code -ne 0 ]; then
        echo -e "\n${RED}>>> STEP ${step_number} FAILED with exit code ${last_exit_code} <<<${NC}\n"
        read -n 1 -s -r -p "Press any key to continue..."
        echo ""
        exit $last_exit_code
    fi
}

# 依次执行各步骤
invoke_step 1 "Font Subsetting & Compression" "script/subset_fonts.py"
invoke_step 2 "Packaging EPUB"                "script/pack_epub.py"
invoke_step 3 "Font Verification"             "script/verify_fonts.py"
invoke_step 4 "XML and EPUB Validation"       "script/validator.py"
invoke_step 5 "EPUBCheck Validation"          "script/epubcheck_validate.py"

echo -e "\n${GREEN}>>> All steps completed successfully! Your final EPUB is in the books/ folder. <<<${NC}\n"


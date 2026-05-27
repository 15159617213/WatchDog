# 微信聊天记录恢复：完整操作指南

## ⚠️ 重要提示

**您需要在自己的手机上执行这些步骤！**

我无法直接访问您的设备，但我会提供详细的操作指导。

---

## 准备工作

### 1. 开启开发者选项和USB调试

**Android设备**：
```
设置 → 关于手机 → 连续点击"版本号"7次 → 返回 → 开发者选项 → 开启USB调试
```

### 2. 安装ADB工具

**Windows**：
- 下载 [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
- 解压到文件夹，添加到系统PATH

**macOS/Linux**：
```bash
# macOS (使用Homebrew)
brew install --cask android-platform-tools

# Linux (Ubuntu/Debian)
sudo apt-get install android-tools-adb
```

---

## 完整操作步骤

### 步骤1：连接设备并检查

```bash
# 在电脑终端执行
adb devices

# 应该看到类似输出：
# List of devices attached
# XXXXXXXXXXXX    device
```

### 步骤2：获取Root权限（如果需要）

```bash
# 进入设备shell
adb shell

# 尝试获取Root
su
# 如果成功，命令提示符会变成 #
```

**如果无法Root，跳过此步，尝试其他恢复方法**。

### 步骤3：查找微信数据

```bash
# 在adb shell中执行

# 进入微信数据目录
cd /data/data/com.tencent.mm/

# 查看目录结构
ls -la
```

### 步骤4：获取UIN（关键步骤）

```bash
# 进入shared_prefs目录
cd /data/data/com.tencent.mm/shared_prefs/

# 查看所有xml文件
ls -la *.xml

# 查找包含uin的文件（可能在system_config_prefs.xml或其他文件中）
cat system_config_prefs.xml | grep uin

# 或者搜索所有xml文件
grep -r "uin" *.xml

# 记录下找到的uin值（纯数字）
```

**可能的UIN位置**：
- `system_config_prefs.xml`
- `auth_info_key_prefs.xml`
- `wx_file_pref.xml`

### 步骤5：获取IMEI或Android ID

```bash
# 方法1：获取IMEI（需要READ_PHONE_STATE权限）
service call iphonesubinfo 1

# 方法2：获取Android ID（更可靠）
settings get secure android_id

# 记录下这个值
```

### 步骤6：查找用户ID文件夹

```bash
# 进入MicroMsg目录
cd /data/data/com.tencent.mm/MicroMsg/

# 查看所有文件夹
ls -la

# 找到那个很长的32位哈希文件夹（这是你的用户ID）
# 通常是类似：a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6

# 进入该文件夹
cd [你的32位用户ID文件夹]/

# 查看数据库文件
ls -la EnMicroMsg*
```

### 步骤7：提取数据库文件

```bash
# 复制到SD卡
cp EnMicroMsg.db /sdcard/
cp EnMicroMsg.db-wal /sdcard/  # 重要！可能包含最新数据
cp EnMicroMsg.db-shm /sdcard/

# 退出shell
exit

# 在电脑终端拉取文件
adb pull /sdcard/EnMicroMsg.db ./
adb pull /sdcard/EnMicroMsg.db-wal ./
adb pull /sdcard/EnMicroMsg.db-shm ./
```

---

## 数据库解密脚本

### Python解密工具

```python
# wechat_decrypt.py
import hashlib
import hmac
import struct
import sys
import os

def calculate_key(imei, uin):
    """计算微信数据库密钥"""
    combined = str(imei) + str(uin)
    md5 = hashlib.md5(combined.encode('utf-8')).hexdigest()
    return md5[:7]

def decrypt_db(input_db, output_db, key):
    """使用SQLCipher解密数据库"""
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("需要安装 pysqlcipher3: pip install pysqlcipher3")
        print("或者使用 DB Browser for SQLite (带SQLCipher支持)")
        return False
    
    conn = sqlite.connect(input_db)
    c = conn.cursor()
    
    # 设置密钥
    c.execute(f"PRAGMA key = '{key}';")
    
    # 设置兼容性（根据微信版本调整）
    c.execute("PRAGMA cipher_compatibility = 3;")
    c.execute("PRAGMA kdf_iter = 4000;")
    
    try:
        # 测试是否能打开
        c.execute("SELECT count(*) FROM sqlite_master;")
        print("✓ 数据库解密成功！")
        
        # 导出到新数据库
        c.execute(f"ATTACH DATABASE '{output_db}' AS plaintext KEY '';")
        c.execute("SELECT sqlcipher_export('plaintext');")
        c.execute("DETACH DATABASE plaintext;")
        
        print(f"✓ 已导出到: {output_db}")
        return True
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("可能的原因：")
        print("1. 密钥不正确")
        print("2. 微信版本不同，加密参数需要调整")
        print("3. 数据库文件已损坏")
        return False

if __name__ == "__main__":
    print("=== 微信数据库解密工具 ===\n")
    
    if len(sys.argv) < 4:
        print("使用方法:")
        print("  python wechat_decrypt.py <数据库文件> <IMEI/AndroidID> <UIN>")
        print("\n示例:")
        print("  python wechat_decrypt.py EnMicroMsg.db 1234567890 987654321")
        sys.exit(1)
    
    db_file = sys.argv[1]
    imei = sys.argv[2]
    uin = sys.argv[3]
    
    if not os.path.exists(db_file):
        print(f"错误: 文件不存在: {db_file}")
        sys.exit(1)
    
    print(f"数据库文件: {db_file}")
    print(f"IMEI/AndroidID: {imei}")
    print(f"UIN: {uin}\n")
    
    key = calculate_key(imei, uin)
    print(f"计算得到密钥: {key}\n")
    
    output_file = os.path.splitext(db_file)[0] + "_decrypted.db"
    
    decrypt_db(db_file, output_file, key)
```

---

## 查看聊天记录

### 使用DB Browser for SQLite

1. 下载并安装 [DB Browser for SQLite](https://sqlitebrowser.org/)
2. 打开解密后的数据库文件
3. 查看主要表：
   - `message` - 聊天消息
   - `rcontact` - 联系人
   - `chatroom` - 群聊信息

### 常用SQL查询

```sql
-- 查看所有消息（按时间倒序）
SELECT msgId, talker, content, createTime 
FROM message 
ORDER BY createTime DESC 
LIMIT 100;

-- 查找特定联系人的聊天
SELECT * FROM message 
WHERE talker = '[联系人微信号]'
ORDER BY createTime DESC;

-- 查找包含特定关键词的消息
SELECT * FROM message 
WHERE content LIKE '%关键词%';
```

---

## 如果无法Root的替代方案

### 方案A：电脑端微信备份恢复

```
1. 登录电脑版微信
2. 左下角 → 备份与恢复
3. 查看是否有历史备份
4. 如果有，恢复到手机
```

### 方案B：专业数据恢复软件

推荐工具：
- 极风数据恢复中心
- EaseUS MobiSaver
- Dr.Fone

### 方案C：手机云备份

- 华为云、小米云、OPPO云等
- 检查是否有微信数据备份

---

## 注意事项

1. **立即停止使用微信** - 防止数据被覆盖
2. **先备份整个手机** - 操作前做完整备份
3. **法律合规** - 仅恢复自己的数据，不要侵犯他人隐私
4. **数据安全** - 恢复后妥善保管数据

---

## 需要帮助？

如果在操作中遇到问题，请告诉我：
1. 您的手机品牌和型号
2. Android版本
3. 具体在哪一步遇到问题
4. 错误信息（如果有）

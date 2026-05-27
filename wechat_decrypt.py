#!/usr/bin#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import p#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter =#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAG#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 400#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY ''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId,#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "←#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("="#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            WHERE#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            WHERE talker LIKE ?
            ORDER BY createTime DESC 
            LIMIT ?
        """, (#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            WHERE talker LIKE ?
            ORDER BY createTime DESC 
            LIMIT ?
        """, (f"%{talker_name}%", limit))
        
        messages = cursor.fetchall()
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            WHERE talker LIKE ?
            ORDER BY createTime DESC 
            LIMIT ?
        """, (f"%{talker_name}%", limit))
        
        messages = cursor.fetchall()
        
        if not messages:
            print(f"未找到与 '{talker_name}' 相关#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            WHERE talker LIKE ?
            ORDER BY createTime DESC 
            LIMIT ?
        """, (f"%{talker_name}%", limit))
        
        messages = cursor.fetchall()
        
        if not messages:
            print(f"未找到与 '{talker_name}' 相关的聊天记录")
            return
        
        print(f"找到 {len(messages)} 条#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信聊天记录数据库解密工具
基于SQLCipher
"""

import hashlib
import sys
import os
import argparse


def calculate_wechat_db_key(imei, uin):
    """
    计算微信数据库密钥
    imei: 设备IMEI（或Android ID）
    uin: 微信用户UIN（可从shared_prefs中获取）
    """
    combined = str(imei) + str(uin)
    md5_hash = hashlib.md5(combined.encode('utf-8')).hexdigest()
    key = md5_hash[:7]  # 取前7位
    return key


def try_decrypt_with_sqlcipher(db_path, key, output_path=None):
    """
    尝试使用SQLCipher解密数据库
    """
    if output_path = output_path or db_path.replace('.db', '_decrypted.db')
    
    try:
        import pysqlcipher3
        from pysqlcipher3 import dbapi2 as sqlite
    except ImportError:
        print("❌ 需要安装 pysqlcipher3")
        print("安装命令: pip install pysqlcipher3")
        print("\n或者使用 DB Browser for SQLite (带SQLCipher支持):")
        print("  https://sqlitebrowser.org/")
        return False
    
    print(f"\n📁 数据库文件: {db_path}")
    print(f"🔑 使用密钥: {key}")
    print(f"📤 输出文件: {output_path}")
    print("-" * 50)
    
    try:
        conn = sqlite.connect(db_path)
        c = conn.cursor()
        
        # 设置密钥
        c.execute(f"PRAGMA key = '{key}';")
        
        # 根据微信版本尝试不同的加密参数
        encryption_params = [
            ("PRAGMA cipher_compatibility = 3;", "PRAGMA kdf_iter = 4000;"),
            ("PRAGMA cipher_compatibility = 4;", "PRAGMA kdf_iter = 64000;"),
            ("PRAGMA cipher_compatibility = 2;", "PRAGMA kdf_iter = 4000;"),
        ]
        
        success = False
        for param1, param2 in encryption_params:
            try:
                c.execute(param1)
                c.execute(param2)
                
                # 测试是否能打开
                c.execute("SELECT count(*) FROM sqlite_master;")
                print("✓ 数据库解密成功！")
                
                # 导出到新数据库
                c.execute(f"ATTACH DATABASE '{output_path}' AS plaintext KEY '';")
                c.execute("SELECT sqlcipher_export('plaintext');")
                c.execute("DETACH DATABASE plaintext;")
                
                print(f"✓ 已成功导出到: {output_path}")
                success = True
                break
            except Exception as e:
                print(f"✗ 尝试参数组合失败: {e}")
                continue
        
        if not success:
            print("✗ 所有加密参数尝试失败")
            return False
        
        # 查看主要表
        print("\n📊 数据库表结构:")
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        for table in tables:
            print(f"  - {table[0]}")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ 解密失败: {e}")
        print("\n可能的原因:")
        print("  1. 密钥不正确")
        print("  2. 微信版本不同，加密参数需要调整")
        print("  3. 数据库文件已损坏")
        return False


def query_messages(db_path, limit=50):
    """
    查询并显示聊天消息
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n📋 查询最近 {limit} 条消息:")
    print("=" * 80)
    
    try:
        # 查询消息表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='message';")
        if not cursor.fetchone():
            print("✗ 未找到 message 表")
            return
        
        # 查询消息
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            ORDER BY createTime DESC 
            LIMIT ?
        """, (limit,))
        
        messages = cursor.fetchall()
        
        if not messages:
            print("未找到消息记录")
            return
        
        print(f"找到 {len(messages)} 条消息:\n")
        
        for msg in messages:
            msg_id, talker, content, create_time, msg_type, is_send = msg
            direction = "→ 发送" if is_send else "← 接收"
            print(f"[{direction} {talker}")
            print(f"  内容: {content}")
            print(f"  时间: {create_time}")
            print("-" * 50)
        
    except Exception as e:
        print(f"查询失败: {e}")
    finally:
        conn.close()


def search_by_talker(db_path, talker_name, limit=100):
    """
    按联系人查询聊天记录
    """
    import sqlite3
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n🔍 查询与 '{talker_name}' 的聊天记录:")
    print("=" * 80)
    
    try:
        cursor.execute("""
            SELECT msgId, talker, content, createTime, type, isSend 
            FROM message 
            WHERE talker LIKE ?
            ORDER BY createTime DESC 
            LIMIT ?
        """, (f"%{talker_name}%", limit))
        
        messages = cursor.fetchall()
        
        if not messages:
            print(f"未找到与 '{talker_name}' 相关的聊天记录")
            return
        
        print(f"找到 {len(messages)} 条相关消息:\n")
        
        for msg in messages:
            msg_id, talker,
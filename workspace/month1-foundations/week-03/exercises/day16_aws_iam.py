#!/usr/bin/env python3
"""
Day 16: AWS Account Setup & IAM
================================
Duration: 2 hours

Set up your AWS account securely and understand IAM fundamentals.
This is the foundation for all cloud work.

WHY THIS MATTERS:
- AWS is the #1 cloud platform for data engineering
- IAM security knowledge is mandatory
- Bad IAM = security breaches, massive bills
- This is always an interview topic

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
from typing import Dict, List, Optional

# =============================================================================
# AWS SETUP EXERCISES (Do these in AWS Console)
# =============================================================================

"""
EXERCISE 1: AWS Account Setup (20 min)
======================================

If you don't have an AWS account:

1. Go to https://aws.amazon.com/free/
2. Click "Create a Free Account"
3. Enter email, password, account name
4. Choose "Personal" account type
5. Enter payment info (required, but free tier won't charge)
6. Verify phone number
7. Choose "Basic Support" (free)

IMPORTANT SECURITY STEPS:
- Enable MFA on root account immediately
- Never use root account for daily work
- Create an IAM user for yourself


EXERCISE 2: Enable MFA on Root Account (10 min)
================================================

This is CRITICAL. Root account with no MFA = disaster waiting.

1. Sign in to AWS Console as root
2. Click your account name (top right) → Security credentials
3. Under MFA, click "Assign MFA device"
4. Choose "Authenticator app"
5. Scan QR code with your phone's authenticator app
6. Enter two consecutive codes
7. Click "Assign MFA"

✅ Your root account is now protected.


EXERCISE 3: Create IAM Admin User (20 min)
==========================================

Never use root for daily work. Create an admin user:

1. Go to IAM service (search "IAM" in console)
2. Click "Users" → "Create user"
3. User name: your-name-admin (e.g., "dante-admin")
4. Select "Provide user access to the AWS Management Console"
5. Choose "I want to create an IAM user"
6. Set a strong password
7. Click "Next"

Attach permissions:
8. Select "Attach policies directly"
9. Search and check "AdministratorAccess"
10. Click "Next" → "Create user"

Set up MFA for this user too:
11. Click on the user → "Security credentials"
12. Assign MFA device (same as root)


EXERCISE 4: Create Programmatic Access (15 min)
================================================

For CLI/SDK access:

1. Go to IAM → Users → your admin user
2. "Security credentials" tab
3. Under "Access keys", click "Create access key"
4. Choose "Command Line Interface (CLI)"
5. Check the acknowledgment
6. Click "Create access key"
7. DOWNLOAD the CSV or copy both keys NOW

Configure AWS CLI:
8. Install AWS CLI (if not already):
   pip install awscli
   # or: brew install awscli (Mac)

9. Configure:
   aws configure
   
   Enter:
   - Access Key ID: (paste)
   - Secret Access Key: (paste)
   - Default region: us-east-1 (or your preference)
   - Output format: json

10. Test:
    aws sts get-caller-identity

SECURITY:
- NEVER commit access keys to git
- Add to .gitignore: .aws/, *.pem, *credentials*
- Rotate keys every 90 days


EXERCISE 5: Understanding IAM Policies (20 min)
================================================

IAM Policies are JSON documents that define permissions.

Structure:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",           # or "Deny"
            "Action": "s3:GetObject",    # What action
            "Resource": "arn:aws:s3:::my-bucket/*"  # On what
        }
    ]
}

Key concepts:
- Principal: Who (user, role, service)
- Action: What they can do (s3:GetObject, lambda:InvokeFunction)
- Resource: What they can do it on (specific bucket, all buckets)
- Effect: Allow or Deny
- Condition: Optional restrictions (IP, time, MFA)

Practice reading policies:
1. Go to IAM → Policies
2. Find "AmazonS3ReadOnlyAccess"
3. Click on it → "Policy document"
4. Read and understand what it allows

Write a simple policy (in Policy editor):
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::my-data-bucket",
                "arn:aws:s3:::my-data-bucket/*"
            ]
        }
    ]
}


EXERCISE 6: Create Data Engineering Role (20 min)
==================================================

Roles are for services/applications, not humans.

1. Go to IAM → Roles → "Create role"
2. Trusted entity: AWS service
3. Use case: Lambda
4. Click "Next"

Attach policies:
5. Search and select:
   - AmazonS3FullAccess
   - AWSLambdaBasicExecutionRole
6. Click "Next"
7. Role name: data-pipeline-role
8. Description: "Role for data pipeline Lambda functions"
9. Click "Create role"

This role can now be assumed by Lambda functions.


EXERCISE 7: Set Up Billing Alerts (15 min)
==========================================

VERY IMPORTANT - avoid surprise bills!

1. Go to Billing (account name → Billing Dashboard)
2. Click "Billing preferences" (left sidebar)
3. Check "Receive Free Tier Usage Alerts"
4. Enter your email
5. Save preferences

Create a billing alarm:
6. Go to CloudWatch service
7. Click "Alarms" → "Create alarm"
8. Click "Select metric"
9. Choose "Billing" → "Total Estimated Charge"
10. Select "USD" metric
11. Click "Select metric"
12. Threshold: Static, Greater than, 5 (dollars)
13. Create an SNS topic for alerts
14. Enter your email
15. Name: "billing-alert-5-dollars"
16. Create alarm
17. Confirm the email subscription
"""

# =============================================================================
# AWS HELPER FUNCTIONS
# =============================================================================

def check_aws_credentials() -> Dict[str, bool]:
    """
    Check if AWS credentials are configured.
    
    Returns:
        Dict with status of credentials, region, and profile
    """
    result = {
        "credentials_file_exists": False,
        "config_file_exists": False,
        "access_key_set": False,
        "region_set": False
    }
    
    # Check for credentials file
    creds_path = os.path.expanduser("~/.aws/credentials")
    result["credentials_file_exists"] = os.path.exists(creds_path)
    
    # Check for config file
    config_path = os.path.expanduser("~/.aws/config")
    result["config_file_exists"] = os.path.exists(config_path)
    
    # Check environment variables
    result["access_key_set"] = bool(os.environ.get("AWS_ACCESS_KEY_ID"))
    result["region_set"] = bool(os.environ.get("AWS_DEFAULT_REGION") or 
                                os.environ.get("AWS_REGION"))
    
    return result


def verify_aws_access() -> Optional[Dict]:
    """
    Verify AWS access by calling STS GetCallerIdentity.
    
    Returns:
        Identity info if successful, None if failed
    """
    try:
        import subprocess
        result = subprocess.run(
            ["aws", "sts", "get-caller-identity"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            import json
            return json.loads(result.stdout)
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# =============================================================================
# IAM POLICY TEMPLATES
# =============================================================================

POLICY_TEMPLATES = {
    "s3_read_only": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::BUCKET_NAME",
                    "arn:aws:s3:::BUCKET_NAME/*"
                ]
            }
        ]
    },
    
    "s3_read_write": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:DeleteObject",
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::BUCKET_NAME",
                    "arn:aws:s3:::BUCKET_NAME/*"
                ]
            }
        ]
    },
    
    "lambda_basic": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:*:*:*"
            }
        ]
    },
    
    "data_engineer": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "S3Access",
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": "*"
            },
            {
                "Sid": "LambdaAccess",
                "Effect": "Allow",
                "Action": "lambda:*",
                "Resource": "*"
            },
            {
                "Sid": "GlueAccess",
                "Effect": "Allow",
                "Action": "glue:*",
                "Resource": "*"
            },
            {
                "Sid": "CloudWatchLogs",
                "Effect": "Allow",
                "Action": [
                    "logs:*"
                ],
                "Resource": "*"
            }
        ]
    }
}


def get_policy_template(name: str, bucket_name: str = "your-bucket") -> Dict:
    """
    Get a policy template with bucket name filled in.
    
    Args:
        name: Policy template name
        bucket_name: S3 bucket name to use
    
    Returns:
        Policy document
    """
    import json
    
    if name not in POLICY_TEMPLATES:
        available = ", ".join(POLICY_TEMPLATES.keys())
        raise ValueError(f"Unknown template. Available: {available}")
    
    policy = POLICY_TEMPLATES[name]
    policy_str = json.dumps(policy).replace("BUCKET_NAME", bucket_name)
    return json.loads(policy_str)


def print_policy(policy: Dict) -> None:
    """Pretty print a policy document."""
    import json
    print(json.dumps(policy, indent=2))


# =============================================================================
# IAM QUIZ
# =============================================================================

def iam_quiz() -> None:
    """Test your IAM knowledge."""
    questions = [
        {
            "q": "What's the FIRST thing you should do after creating an AWS account?",
            "options": [
                "Create an S3 bucket",
                "Enable MFA on root account",
                "Launch an EC2 instance",
                "Create a Lambda function"
            ],
            "answer": 1,
            "explanation": "Always secure root account with MFA first. Root account compromise is catastrophic."
        },
        {
            "q": "Should you use the root account for daily work?",
            "options": [
                "Yes, it has all permissions",
                "Only for S3 access",
                "No, create an IAM user",
                "Only on weekends"
            ],
            "answer": 2,
            "explanation": "Never use root for daily work. Create IAM users/roles with least privilege."
        },
        {
            "q": "What's the difference between IAM Users and Roles?",
            "options": [
                "No difference",
                "Users are for humans, Roles are for services",
                "Roles are more secure",
                "Users are free, Roles cost money"
            ],
            "answer": 1,
            "explanation": "Users = humans with credentials. Roles = temporary credentials for services/apps."
        },
        {
            "q": "What does the 'Principal' in an IAM policy specify?",
            "options": [
                "The action to perform",
                "The resource to act on",
                "Who/what can perform the action",
                "The cost of the action"
            ],
            "answer": 2,
            "explanation": "Principal = who can perform the action (user, role, service, account)."
        },
        {
            "q": "Where should you NEVER store AWS access keys?",
            "options": [
                "AWS credentials file",
                "Environment variables",
                "Git repository",
                "AWS Secrets Manager"
            ],
            "answer": 2,
            "explanation": "Never commit keys to git! Use environment variables, credentials file, or secrets manager."
        }
    ]
    
    print("=" * 60)
    print("IAM KNOWLEDGE QUIZ")
    print("=" * 60 + "\n")
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"  {j+1}. {opt}")
        
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if answer == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. {q['explanation']}\n")
        except:
            print(f"Invalid input. {q['explanation']}\n")
    
    print("=" * 60)
    print(f"Score: {score}/{len(questions)}")
    print("=" * 60)


# =============================================================================
# Verification
# =============================================================================

def verify_aws_setup() -> None:
    """Verify AWS setup is complete."""
    print("=" * 60)
    print("AWS SETUP VERIFICATION")
    print("=" * 60 + "\n")
    
    # Check credentials
    creds = check_aws_credentials()
    
    if creds["credentials_file_exists"]:
        print("✅ AWS credentials file exists")
    else:
        print("❌ No credentials file. Run: aws configure")
    
    if creds["config_file_exists"]:
        print("✅ AWS config file exists")
    else:
        print("⚠️  No config file (optional)")
    
    # Test API access
    print("\nTesting AWS API access...")
    identity = verify_aws_access()
    
    if identity:
        print(f"✅ AWS access verified!")
        print(f"   Account: {identity.get('Account')}")
        print(f"   User/Role: {identity.get('Arn')}")
    else:
        print("❌ Cannot access AWS. Check credentials.")
    
    print("\n" + "-" * 40)
    print("Checklist:")
    print("[ ] MFA enabled on root account")
    print("[ ] IAM admin user created")
    print("[ ] MFA enabled on IAM user")
    print("[ ] AWS CLI configured")
    print("[ ] Billing alert set up")
    print("-" * 40)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "quiz":
            iam_quiz()
        elif cmd == "verify":
            verify_aws_setup()
        elif cmd == "policy":
            name = sys.argv[2] if len(sys.argv) > 2 else "s3_read_only"
            bucket = sys.argv[3] if len(sys.argv) > 3 else "my-bucket"
            print_policy(get_policy_template(name, bucket))
        elif cmd == "templates":
            print("Available policy templates:")
            for name in POLICY_TEMPLATES:
                print(f"  - {name}")
    else:
        print("Day 16: AWS Account Setup & IAM")
        print("=" * 40)
        print("\nThis is an AWS Console-focused day.")
        print("Follow the exercises in the AWS Console.")
        print("\nCommands:")
        print("  python day16_aws_iam.py quiz      - Take the IAM quiz")
        print("  python day16_aws_iam.py verify    - Verify your setup")
        print("  python day16_aws_iam.py templates - List policy templates")
        print("  python day16_aws_iam.py policy <name> [bucket] - Show policy")

"""
Sanitized extract from DentSignal's historical FastAPI admin routes.

Source:
  6eb60ec15dcc286a5234c8e6de84174d280b8951

The surrounding clinic CRUD/auth code was removed here. This file only shows
the Twilio install/maintenance surface that existed in the private project.
"""

from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from twilio_number_provisioning import (
    list_available_numbers as twilio_list_numbers,
    provision_clinic_number,
    release_number,
    update_number_webhooks,
)

router = APIRouter(prefix="/api", tags=["Admin"])


class ProvisionNumberRequest(BaseModel):
    clinic_id: int
    area_code: Optional[str] = None
    phone_number: Optional[str] = None
    friendly_name: Optional[str] = None


@router.get("/admin/available-numbers")
async def available_numbers(
    area_code: Optional[str] = Query(None),
    limit: int = Query(10, ge=1, le=50),
):
    result = twilio_list_numbers(area_code=area_code, limit=limit)
    return {
        "available_numbers": result,
        "count": len(result),
    }


@router.post("/admin/provision-number")
async def provision_number(request: ProvisionNumberRequest):
    """Purchase a number and configure voice/SMS/status webhooks."""

    result = provision_clinic_number(
        clinic_id=request.clinic_id,
        area_code=request.area_code,
        phone_number=request.phone_number,
        friendly_name=request.friendly_name,
    )

    if not result.get("success"):
        raise HTTPException(status_code=500, detail="Failed to provision number")

    # Original route persisted the returned number/SID against the clinic record.
    return {
        "success": True,
        "clinic_id": request.clinic_id,
        "phone_number": result["phone_number"],
        "twilio_sid": result["sid"],
        "webhooks": result["webhooks"],
    }


@router.post("/admin/fix-webhooks/{phone_sid}")
async def fix_number_webhooks(phone_sid: str):
    result = update_number_webhooks(phone_sid)

    if not result.get("success"):
        raise HTTPException(status_code=500, detail="Failed to update webhooks")

    return result


@router.delete("/admin/release-number/{phone_sid}")
async def release_phone_number(phone_sid: str):
    result = release_number(phone_sid)

    if not result.get("success"):
        raise HTTPException(status_code=500, detail="Failed to release number")

    return result
